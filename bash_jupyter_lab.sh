cp Dockerfile.bash Dockerfile
sudo docker build -t ibash .
sudo docker run --rm --name bash_jupyter_lab -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v $JUPYTER_WORKSPACE:/home/jovyan/work ibash
