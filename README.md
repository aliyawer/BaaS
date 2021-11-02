# BaaS
This is BENCHOP-as-a-service (BaaS).

BENCHOP is a benchmarking project in option pricing, initiated by the Computational Finance research group at the division of Scientific Computing at Uppsala University. The aim of BENCHOP is to provide the finance community with a set of common benchmark problems that can be used both for comparisons between methods and for evaluation of new methods for option pricing. BENCHOP is defined as six problems that are solved using MATLAB implementations of fifteen numerical methods. Since each problem is solved using complex mathematical functions, the execution takes a long time when running all problems at once, one after the other. 

BaaS aims at speeding up the execution of the problems by running different solvers in parallel in the backend on different instances on the openstack cloud. 

## How to create the virtual machines 
After cloning this repository you can follow these steps to setup the instances. 

1) Navigate to the same folder as main.tf
  ```shell
  cd BaaS
  ```
2) Generate a key pair by running the following command and name it `myKey`.
  ```shell
  ssh-keygen -b 2048 -t rsa
  ```
3) Create a file called `secret.tfvars` and add key_pair = "myKey". The following should be the content of the `secret.tfvars` file.
  ```shell
  key_pair = "myKey"
  ```
4) Source the openstack resource file <project_name>.openrc.sh exchanging `<project_name>` by the name of the openstack resource project file name.
  ```shell
  source <project_name>.openrc.sh
  ```
5) Install Terraform. Look at the following link to see instruction on how to install it on your OS: https://learn.hashicorp.com/tutorials/terraform/install-cli
6) Then run the following commands to start the instances with terraform. Replacing `Number of workers` with an actual integer value. 
  ```shell
  terraform init
  terraform apply -var-file="secret.tfvars" -var="workers=Number of workers"
  ```

The initialization may take at least 30 minutes, up to 50 minutes, to complete. 

## Usage
After the virtual machines has been initialized the service can be reached by entering the following in a browser, exchanging `<ip-address>` with the actual floating ip address of the producer instance.
  
```shell
  http://<ip-address>:5000/baas
```
  
  The celery workers can be seen by entering the following, again you have to exchange the `<ip-address>`.
  
```shell
  http://<ip-address>:5555
```

## Delete the instances
To take down the instances when you are done, you can run the following command.
```shell
terraform destroy -var-file="secret.tfvars"
```
