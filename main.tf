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

resource "openstack_compute_instance_v2" "BaaS-terraform-producer" {
  name            = "BaaS-terraform-producer"
  image_name      = "Ubuntu 18.04"
  flavor_name     = "ssc.medium"
  key_pair        = "myKey"
  security_groups = ["default", "BaaS-security-group"]
  user_data = file("cloudinit/cloud-config-producer.txt")

  network {
    name = "UPPMAX 2021/1-5 Internal IPv4 Network"
  }
}

resource "openstack_networking_floatingip_v2" "floatip_1" {
  pool = "Public External IPv4 Network"
}

resource "openstack_compute_floatingip_associate_v2" "floatip_1" {
  floating_ip = "${openstack_networking_floatingip_v2.floatip_1.address}"
  instance_id = "${openstack_compute_instance_v2.BaaS-terraform-producer.id}"


}

