# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration: create a file named: config.cfg in same folder with file Server.py. And then add configurations to this file

```
#!Plain Text

[DEFAULT]
tcp_port = [TCP Port]
web_port = [Web Port]
websocket_port = [Web Socket Port]
db_host = [Database host]
db_port = [Database port]
db_name = [Database name]
#  Uncomment to use authentication of database.
; db_user = [User to connect db]
; db_password = [Password of user connect db]
; db_authentication_source = [Authentication source]
```

* Dependencies: all python libraries are placed in file *requirement.txt*. And below is steps to install dependency.

```
#!Plain Text
   1.  Install python-dev: sudo apt-get install python-dev
   2.  Install all packages in requirement.txt: sudo pip install -r requirements.txt
   3.  Copy file libs/websockets.py to folder /usr/local/lib/python2.7/dist-packages/twisted/web

```
* Database configuration
* To run NFC Server: use terminal and type:

```
#!Plain Text
python Server.py

```

* Deployment instructions: NFC server use [Upstart](https://www.digitalocean.com/community/tutorials/the-upstart-event-system-what-it-is-and-how-to-use-it) to start as a service. To config upstart to run NFC server:

```
#!Plain Text

1. Create a folder name nfc-server in /opt. Then cd to that folder.
2. Clone source code from bitbucket (using https or ssh protocol), then cd to folder touchterminal-server.
2. Copy file scripts/nfc-server.conf to folder /etc/init, then type command: sudo chmod 775 /etc/nfc-server.conf
3. To start NFC service: sudo service nfc-server start
4. To stop NFC service: sudo service nfc-server stop
5. To restart NFC service: sudo service nfc-server restart
```


### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact