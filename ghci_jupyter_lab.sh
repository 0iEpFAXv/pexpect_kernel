cp Dockerfile.ghci Dockerfile
sudo docker build -t ighci .
#sudo docker run --rm --name ghci_jupyter_lab -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v $JOVYAN_STACK_PATH:/home/jovyan/.stack -v $JUPYTER_WORKSPACE:/home/jovyan/work ighci
sudo docker run --rm --name ghci_jupyter_lab -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v $JOVYAN_STACK_PATH:/home/jovyan/.stack -v $JUPYTER_WORKSPACE:/home/jovyan/work --entrypoint=start.sh ighci jupyter lab --watch
