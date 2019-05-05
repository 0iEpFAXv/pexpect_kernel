sudo docker build -t tbilltechrep/ighci -f Dockerfile.ghci-stack .
sudo docker push tbilltechrep/ighci 
#sudo docker run --rm --name ghci_jupyter_lab -p 8888:8888 -v $JOVYAN_STACK_PATH:/home/jovyan/.stack -v $JUPYTER_WORKSPACE:/home/jovyan/work tbilltechrep/ighci
sudo docker run --rm --name ghci_jupyter -p 8888:8888 -v $JOVYAN_STACK_PATH:/home/hie/.stack -v $JUPYTER_WORKSPACE:/home/hie/work tbilltechrep/ighci
