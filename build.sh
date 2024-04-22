cd Cadiz_Peiffer_ec2
docker build -t web_counter .
docker run -d -p 80:80 -v "$(pwd)/data":/app/data --name web_counter web_counter
