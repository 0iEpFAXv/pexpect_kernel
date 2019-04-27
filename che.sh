#sudo docker run -it --rm \
#     -v /var/run/docker.sock:/var/run/docker.sock \
#     -v /home/che:/data \
#     -v /home/tom/code:/data/workspaces \
#     -e CHE_HOST=192.168.0.121 \
#     eclipse/che start

sudo docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock -v /home/che:/data eclipse/che start
