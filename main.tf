# Define required providers
terraform {
required_version = ">= 0.14.0"
  required_providers {
    openstack = {
      source  = "terraform-provider-openstack/openstack"
      version = "~> 1.35.0"
    }
    docker = {
      source  = "kreuzwerker/docker"
      version = ">= 2.13.0"
    }
  }
}

# Configure the OpenStack Provider
provider "openstack" {
  auth_url = "https://east-1.cloud.snic.se:5000/v3"
}

# Producer instance
resource "openstack_compute_instance_v2" "BaaS-terraform-producer" {
  name            = "BaaS-terraform-producer"
  image_name      = "Ubuntu 18.04"
  flavor_name     = "ssc.medium"
  key_pair        = var.key_pair
  security_groups = ["default", "BaaS-security-group"]
  user_data = file("cloudinit/cloud-config-producer.txt")

  network {
    name = "UPPMAX 2021/1-5 Internal IPv4 Network"
  }
}

resource "openstack_networking_floatingip_v2" "producer_floatingip" {
  pool = "Public External IPv4 Network"
}

resource "openstack_compute_floatingip_associate_v2" "producer_floatingip" {
  floating_ip = "${openstack_networking_floatingip_v2.producer_floatingip.address}"
  instance_id = "${openstack_compute_instance_v2.BaaS-terraform-producer.id}"
}

# Worker instance
resource "openstack_compute_instance_v2" "BaaS-terraform-worker" {
  count           = var.workers
  name            = join("-",["BaaS-terraform-worker", count.index])
  image_name      = "Ubuntu 18.04"
  flavor_name     = "ssc.medium"
  key_pair        = var.key_pair
  security_groups = ["default", "BaaS-security-group"]
  user_data       = file("cloudinit/cloud-config-worker.txt")

  network {
    name = "UPPMAX 2021/1-5 Internal IPv4 Network"
  }

  depends_on = [
    openstack_compute_instance_v2.BaaS-terraform-producer
  ]
}

resource "openstack_networking_floatingip_v2" "worker_floatingip" {
  pool  = "Public External IPv4 Network"
  count = var.workers
}

resource "openstack_compute_floatingip_associate_v2" "worker_floatingip" {
  count       = var.workers
  floating_ip = "${openstack_networking_floatingip_v2.worker_floatingip[count.index].address}"
  instance_id = "${openstack_compute_instance_v2.BaaS-terraform-worker[count.index].id}"
}

# Set ip of producer to celery worker of worker
resource "null_resource" "set_celery_broker_of_worker" {
  count      = var.workers
  depends_on = [
    openstack_compute_floatingip_associate_v2.producer_floatingip,
    openstack_compute_floatingip_associate_v2.worker_floatingip,
    openstack_compute_instance_v2.BaaS-terraform-producer,
    openstack_compute_instance_v2.BaaS-terraform-worker,
  ]
  connection {
    user = "ubuntu"
    host = openstack_compute_floatingip_associate_v2.worker_floatingip[count.index].floating_ip
    private_key = file("myKey")
  }
  provisioner "remote-exec" {
    inline = [
      "echo \"broker_url = 'amqp://admin:admin@\"${openstack_compute_instance_v2.BaaS-terraform-producer.access_ip_v4}\":5672/vhost'\" > /home/ubuntu/celeryconfig.py",
    ]
  }
} 
