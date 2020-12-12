Bank security console
-----------------------------

Description
-----------
The security console is a site that can be connected to a remote database with visits and pass cards of bank employees.
This repository was created for educational purposes. Module by devman

Requirements
--------------------------
```
python 3.5 +
```

How to install
--------------
Python3 should be already installed.
```
sudo apt-get install python3
sudo apt-get install python3-pip
```
Download project and install dependencies
```
git clone https://github.com/MZen2610/TerminalSecurity.git
cd TerminalSecurity
pip install -r requirements.txt
```
DJANGO_DEBUG on production server must be False. If True, displays detailed error information.
```
DB_HOST = your_host
DB_PORT = your_port
DB_NAME = your_name
DB_USER = your_username
DB_PASSWORD = your_password
DJANGO_SECRET_KEY = your_secret_key
DJANGO_DEBUG = False
```
Run the project
```
python manage.py runserver
```
Go to the address http://127.0.0.1:8000/

Project Goals
-------------

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
