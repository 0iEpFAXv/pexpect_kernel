sudo docker build -t ighci -f Dockerfile.ghci .
sudo docker run --rm --name ghci_jupyter_lab -p 8888:8888 -v $JOVYAN_STACK_PATH:/home/jovyan/.stack -v $JUPYTER_WORKSPACE:/home/jovyan/work ighci
