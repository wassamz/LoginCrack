# LoginCrack
Basic Penetration testing
\

## Step 1 Install and Set up Docker Image
### Install docker 
https://www.docker.com/get-started

### Download Image
Download image of app to be cracked into. \
More details on this image can be found here: https://hub.docker.com/r/vulnerables/web-dvwa/ \
docker pull vulnerables/web-dvwa

### Run the docker container
docker run --rm -it -p 80:80 vulnerables/web-dvwa

### Set up environment
On the first run \
Go to  http://localhost \
Click Create / Reset Database 

## Prepare and Run Python Script
### Install the Python dependencies
sudo pip install requests \
sudo pip install beautifulsoup4

### Run Login Crack Script
Run the python script to find a password that works \
python3 loginCrack.py
