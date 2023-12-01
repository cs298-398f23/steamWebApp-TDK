#!/bin/bash

# Install system packages
sudo yum update -y
sudo yum install python3-pip git -y

# Clone the GitHub repo
git clone https://github.com/cs298-398f23/steamWebApp-TDK.git
cd steamWebApp-TDK/

# Creates and activates a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Installs Python reqs
pip install -r requirements.txt
pip install urllib3==1.26.6

# Install additional system reqs
sudo amazon-linux-extras install epel -y
sudo amazon-linux-extras install redis6 -y

# Starts the Redis-server
redis-server --daemonize yes

# Runs the Python scripts
python3 add_games_to_redis.py
python3 games_app.py
