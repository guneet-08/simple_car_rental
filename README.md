# simple_car_rental
A basic application to rent cars made by using Python, MySQL and is deployed in the Linux Environment

Before starting make sure you have the following dependencies ready:

Install Python: If Python is not already installed on your Linux system, you can install it by running the following command:
```
sudo apt update
sudo apt install python3
```

Install MySQL: Install MySQL on your Linux system by running the following commands:
```
sudo apt update
sudo apt install mysql-server
```

Install the mysql-connector-python package: Use the following command to install the package required for connecting Python to MySQL:
```
pip3 install mysql-connector-python
```

Create the MySQL database: Open a terminal and log in to MySQL as the root user by running the command:
```
sudo mysql -u root -p
```

Enter your MySQL root password when prompted. Once you are logged in to the MySQL prompt, create the database by running the command:
```
CREATE DATABASE car_rental;
```

Now, Create a dirctory and add the car_rental.py and start.sh to that folder.

It is reccomended to create a new user to make connection to the SQL Database (avoid using 'root'@'localhost')

To create a user:
Log in to MySQL as the root user:
```
sudo mysql -u root -p
```

Create a new user for your application and grant necessary privileges:
Replace 'your_username' and 'your_password' with your desired username and password, respectively.

```
CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON car_rental.* TO 'your_username'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

Now, give execution permissions to start.sh and Run the script.



