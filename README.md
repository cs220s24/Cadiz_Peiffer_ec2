# Cadiz_Peiffer_ec2

## Overview
The goal of this project was to implement CI/CD for the Dockerized Web_Counter application. The CI portion of the project is our test.yml file which tests the Web_Counter by using both Flake8 and our test file testServer.py. After the CI portion, our CD portion utilizes the AWS_Redeploy.yml the continuously deploy the changes made to an EC2 instance. However, due to the fact that we utilized the AWS learner lab, we were unable to create permanent instances. Due to this the public IP address of the instance and the user's private key to access the instance must be updated in the redeploy.yml file for continuous deployment to occur(if you are creating your own instance). Although the private key needs to be updated in the yaml file a GitHub secret needs to be made to safeguard the private key. Within the yaml file the secret variable would then be used instead of the actual private key itself and displaying it publicly.

- Contributers: Samuel Cadiz and Jaden Peiffer



![Dev Ops UML (1)](https://github.com/cs220s24/Cadiz_Peiffer_ec2/assets/143456301/5c08a242-f853-4c37-99b7-d9beb96c56c2)



## Get Redeploy Functional
1. Update the AWS IP address in the redeploy.yml
    - Change the remote host to your AWS instance public IP address
  
      `REMOTE HOST: "<AWS IP address>"`
      
2. Update SSH_KEY in the redeploy.yml
   - Create a GitHub secret that has the contents of your private ssh key
   - Update SSH_KEY under "env:" to be your GitHub secret name that includes your ssh key
  
      `SSH_KEY: ${{ secrets.< Your secret name> }}`

## Launch locally
1. Git clone Cadiz_Peiffer_ec2
   
    `git clone Cadiz_Peiffer_ec2`

2. Go into Cadiz_Peiffer_ec2
   
    `cd Cadiz_Peiffer_ec2`
   
3. Create a virtual environment

    `python3 -m venv .venv`

4. Activate the virtual environment

    `source .venv/bin/activate`

5. Install the requirements.txt

    `pip install -r requirements.txt`

6. Run the app.py file
   
   `python app.py`

7. Open a web browser and go to `http://localhost:8000`
   - You can also launch locally using Gunicorn outside the virtual environment
     
     `.venv/bin/gunicorn --bind 0.0.0.0:8000 app:app`
   - Then go to `http://localhost:8000`

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

## Redeploy.sh description:
-  Deletes the docker container 
-  Git pulls any changes made to the repository
-  Rebuilds and runs the docker container on port 80
   
