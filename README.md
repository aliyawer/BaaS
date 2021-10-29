# BaaS
BENCHOP as a service.

## To create your virtual machines 
- Generate a key pair named myKey and place it in the same level as main.tf
- Navigate to same folder as main.tf
- Create a file called secret.tfvars and add key_pair = "myKey"
- Then run the following commands 
--terraform init
--terraform plan
--terraform apply
