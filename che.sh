sudo docker run -it --rm \
     -p 8080:8080 -p 8000:8000 \
     -v /var/run/docker.sock:/var/run/docker.sock \
     -v /home/tom/che_data:/data \
     -v /home/tom/code:/data/workspaces \
     -e CHE_HOST=192.168.0.121 \
     eclipse/che:latest start
