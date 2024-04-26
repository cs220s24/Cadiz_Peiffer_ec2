# Cadiz_Peiffer_ec2
#By: Samuel Cadiz and Jaden Peiffer

## Launch on AWS Instance
1. Create an AWS instance
2. Install git onto AWS instance
   
   `ssh -i ~/.ssh/<private ssh key file> ec2-user@<public IP address of instance> sudo yum install git`
4. Clone GitHub repository
   
   `ssh -i ~/.ssh/<ssh key> ec2-user@<public IP address of instance> git clone https://github.com/cs220s24/Cadiz_Peiffer_ec2.git`
5. Update the AWS IP address in the redeploy.yml and push to origin main
   
   `push origin main AWS_Redeploy.yml`
6. Activate deploy.sh
   - Installs docker and allows ec2-user permissions
     
   `ssh -i ~/.ssh/<ssh key> ec2-user@<public IP address of instance> ./Cadiz_Peiffer_ec2/deploy.sh`
7. Activate build.sh
   - Builds and runs docker container for web_counter on port 80
     
   `ssh -i ~/.ssh/<ssh key> ec2-user@<public IP address of instance> ./Cadiz_Peiffer_ec2/build.sh`
*Note*
- To take down the web_counter:
  
-  `ssh -i ~/.ssh/<ssh key> ec2-user@<public IP address of instance> ./Cadiz_Peiffer_ec2/down`
   
