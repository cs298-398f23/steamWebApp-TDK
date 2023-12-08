# steamWebApp-TDK

### Overview
Final project for CSCI 398 Web Programming. Our project is a flask server that allows you to search games in the Steam library and see their price and recent news.
The server also allows you to add games to a favorites list that shows the game name, Steam ID, and price. The web application also allows you to register an account and saves
credentials in redis so you can login to get your favorites list. 

### Host on EC2

Start up an EC2 instance using Linux AMI 2 and make sure your security group allows HTTP traffic. 
Create a .env file with 2 variables

`
INSTANCE_ID=<EC2 Instance ID>
public_ip=<EC2 Public IP>
`

### Host locally
