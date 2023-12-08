#!/bin/bash

# Install system packages if not already installed
sudo yum update -y
sudo yum install python3-pip git -y

# Clone the GitHub repo if it doesn't already exist
if [ ! -d "steamWebApp-TDK" ]; then
    git clone https://github.com/cs298-398f23/steamWebApp-TDK.git
fi
cd steamWebApp-TDK/

# Create and activate a Python virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
source .venv/bin/activate

# Install Python requirements if not already installed
pip install -r requirements.txt
pip install urllib3==1.26.6

# Check if EPEL and Redis are installed, install if they are not
if ! sudo amazon-linux-extras list | grep -q epel; then
    sudo amazon-linux-extras install epel -y
fi
if ! rpm -q redis; then
    sudo amazon-linux-extras install redis6 -y
fi

# Start the Redis-server
redis-server --daemonize yes

# Run the flask 
sudo /home/ec2-user/steamWebApp-TDK/.venv/bin/python3 /home/ec2-user/steamWebApp-TDK/games_app.py
