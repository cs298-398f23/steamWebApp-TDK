#!/bin/bash

# source from .env (Ec2 Instance ID)
source .env

# Start the EC2 instance 
aws ec2 start-instances --instance-ids $INSTANCE_ID

# Wait for the instance type to be 'running'
aws ec2 wait instance-running --instance-ids $INSTANCE_ID

# Get the public IP address of the instance
public_ip=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID --query "Reservations[0].Instances[0].PublicIpAddress" --output text)

# Copy the 'up.sh' script to the EC2 instance=
scp -i /path/to/your-key.pem up.sh ec2-user@$public_ip:/home/ec2-user

# SSH into the instance and execute the 'up.sh' script remotely
ssh -i /path/to/your-key.pem ec2-user@$public_ip "bash /home/ec2-user/up.sh"

echo "EC2 instance is running, and 'up.sh' script is executed remotely."
