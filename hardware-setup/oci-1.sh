## Update system
echo "--------------  Updating system  --------------"
sudo apt update && sudo apt upgrade -y

##############################
## Install docker and misc. ##
##############################
echo "--------------  Installing docker and misc.  --------------"
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    -y
cd
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y
sudo systemctl enable docker.service
sudo systemctl enable containerd.service

## Check docker and docker-compose
echo "--------------  Checking docker and docker-compose  --------------"
docker -v
docker compose
sudo apt install docker-compose -y

## Adding docker group
echo "--------------  Fixing permissions for Docker CLI  --------------"
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker