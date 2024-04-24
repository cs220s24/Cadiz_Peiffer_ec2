docker rm -f web_counter
cd Cadiz_Peiffer_ec2
git pull origin main
docker build -t web_counter .
docker run -d -p 80:80 -v $(pwd)/data:/app/data --name web_counter web_counter
