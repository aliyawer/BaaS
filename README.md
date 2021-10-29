# BaaS
BENCHOP as a service.

## To create your virtual machines 
1) Generate a key pair named myKey and place it in the same level as main.tf
2) Navigate to same folder as main.tf
3) Create a file called secret.tfvars and add key_pair = "myKey"
4) Then run the following commands 
- terraform init
- terraform plan
- terraform apply
