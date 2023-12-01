#!/bin/bash

# Stops the Flask server
pkill -f games_app

# Deactivates the virtual environment only if active (Python)
if [[ "$VIRTUAL_ENV" != "" ]]
then
    deactivate
fi

# Stops the Redis server
redis-cli shutdown

# Added delay before the shutdown
echo "Waiting for 15 seconds before EC2 shutdown..."
sleep 15

# Confirmation prompt
read -p "Are you sure you want to shutdown the EC2 instance? (yes/no): " confirmation
if [[ $confirmation == "yes" || $confirmation == "Yes" ]]
then
    # Shutting down the EC2 instance
    # Replace 'your-instance-id' with the ID of your EC2 instance (due to learner lab, we can't share the same ec2 as of now)
    aws ec2 stop-instances --instance-ids your-instance-id
    echo "EC2 instance is shutting down."
else
    echo "EC2 shutdown cancelled."
fi
