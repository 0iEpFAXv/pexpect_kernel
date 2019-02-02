cp Dockerfile.ighci Dockerfile
sudo docker build -t ighci .
sudo docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v $JUPYTER_WORKSPACE:/home/jovyan/work ighci
