git clone https://github.com/cs220s24/Cadiz_Peiffer_ec2.git 
sudo yum install -y docker
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ec2-user
exit
