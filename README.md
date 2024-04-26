# Cadiz_Peiffer_ec2
- Contributers: Samuel Cadiz and Jaden Peiffer

## Get Redeploy Functional
1. Update the AWS IP address in the redeploy.yml
    - Change the remote host to your AWS instance public IP address
  
      `REMOTE HOST: "<AWS IP address>"`
      
2. Update SSH_KEY in the redeploy.yml
   - Create a GitHub secret that has the contents of your private ssh key
   - Update SSH_KEY under "env:" to be your GitHub secret name that includes your ssh key
  
      `SSH_KEY: ${{ secrets.< Your secret name> }}`

## Launch on AWS Instance
1. Create an AWS instance
      
2. Install git onto AWS instance
   
   `ssh -i ~/.ssh/<private ssh key file> ec2-user@<public IP address of instance> sudo yum install -y git`
   
3. Clone GitHub repository
   
   `ssh -i ~/.ssh/<ssh key> ec2-user@<public IP address of instance> git clone https://github.com/cs220s24/Cadiz_Peiffer_ec2.git`

4. Activate deploy.sh
   - Installs docker and allows ec2-user permissions
     
   `ssh -i ~/.ssh/<ssh key> ec2-user@<public IP address of instance> ./Cadiz_Peiffer_ec2/deploy.sh`
   
5. Activate build.sh
   - Builds and runs docker container for web_counter on port 80
     
   `ssh -i ~/.ssh/<ssh key> ec2-user@<public IP address of instance> ./Cadiz_Peiffer_ec2/build.sh`
   
## NOTE

- To take down the web_counter:
  
-  `ssh -i ~/.ssh/<ssh key> ec2-user@<public IP address of instance> ./Cadiz_Peiffer_ec2/down`
   
