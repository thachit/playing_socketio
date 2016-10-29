# README #
* Requirement:

```
1. Ubuntu 14.04 or higher
2. python 2.7
3. Source control Git: (sudo apt-get install git)

```
* Install Dependencies: all python libraries are placed in file *requirement.txt*. And below is steps to install dependency.

```
   1.  Install python-dev: sudo apt-get install python-dev libffi-dev libssl-dev
   2.  Install all packages in requirement.txt: sudo pip install -r requirements.txt
   3.  Copy file libs/websockets.py to folder /usr/local/lib/python2.7/dist-packages/twisted/web

```

* 1. Run Server: Open terminal and type:

```
python Server.py

```
 * 2. Run Client: Open other terminal and type:

```
python Client.py

```
 * 3. Access web: using browser
```
http://localhost:6080/

```
 * 4. Test app
In terminal that run Client.py, type any String, This String will be shown on website without refesh webpage.
