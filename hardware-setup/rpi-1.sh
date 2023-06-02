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
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

## Check docker and docker-compose
echo "--------------  Checking docker and docker-compose  --------------"
docker -v
docker compose
sudo apt install docker-compose -y

## Installing portainer
echo "--------------  Installing Portainer BE  --------------"
docker volume create portainer_data
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:latest
echo "
--------------  Portainer is available on IP:9443  --------------
"