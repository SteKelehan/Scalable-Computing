#!/usr/bin/


# udate env
sudo apt update  
sudo apt upgrade  
sudo apt-get install build-essential 
sudo apt-get install linux-image-extra-virtual


# install hashcat
sudo apt install hashcat

# install GPU driver
wget -Os 'NVIDIA_DRIVER.run' 'http://us.download.nvidia.com/tesla/396.44/NVIDIA-Linux-x86_64-396.44.run'
chmod +x ./NVIDIA_DRIVER.run
sudo ./NVIDIA_DRIVER.run -s

# Test Hashcat
hashcat -I


