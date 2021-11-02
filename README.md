# BaaS
BENCHOP as a service.

## To create your virtual machines 
1) Generate a key pair named myKey and place it in the same level as main.tf
2) Navigate to same folder as main.tf
3) Create a file called secret.tfvars and add key_pair = "myKey"
4) Source the openstack resource file <project_name>.openrc.sh
5) Then run the following commands
- terraform init
- terraform apply -var-file="secret.tfvars" -var="workers=Number of workers"

The initialization may take at least 30 minutes to complete. 

## Usage
After completion the service can be reached by entering the following in a browser, exchanging "<ip-address>" with the actual floating ip address of the producer instance.
  
'''shell
  http://<ip-address>:5000/baas
'''
  
  The celery workers can be seen by entering the following, again you have to exchange the "<ip-address>".
  
  '''shell
  http://<ip-address>:5555
  '''
