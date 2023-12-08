# steamWebApp-TDK

### Overview
Final project for CSCI 398 Web Programming. Our project is a flask server that allows you to search games in the Steam library and see their price and recent news.
The server also allows you to add games to a favorites list that shows the game name, Steam ID, and price. The web application also allows you to register an account and saves
credentials in redis so you can login to get your favorites list. 

### Host on EC2

Start up an EC2 instance using Linux AMI 2 and make sure your security group allows HTTP traffic. 
Clone this repo locally and create a .env file with 2 variables

```
INSTANCE_ID=<EC2 Instance ID>
public_ip=<EC2 Public IP>
```
Make sure you have the aws package installed.

`pip install aws`

Change the path to your .pem key in lines 16 and 19 of the UpExp.sh and then run the UpExp.sh file to ssh into the EC2 instance and remotetly run the Up.sh file.

`sh UpExp.sh`

Open a browser and connect to the server using the public IP address of the EC2 and port 80.

`<Public IP>:80`


### Host locally

Clone the repo, start up a virtual environment, and install the requirements.

```
python3 -m .venv venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the games_app.py file.

`python3 games_app.py`

Open a browser and connect to the server using the home IP address and port 8000.

`127.0.0.1:8000`

### Testing
