sudo docker build -t tbilltechrep/hie-ls-machine -f Dockerfile.hie .
echo "see https://www.eclipse.org/che/docs/che-6/language-servers.html for how to use with che"
sudo docker push tbilltechrep/hie-ls-machine
#sudo docker run --rm --name hie-ls-machine -p 4417:4417 tbilltechrep/hie-ls-machine
