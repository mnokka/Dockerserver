# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Flask server, using application server uwsgi
* Tested Virtual box + Ubuntu 16.4 LTS (Host Windows10)


### How do I get set up? ###

* Install Docker   https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-repository
* Do not use Ambientia VPN
* Clone repo and execute in root
* sudo docker build -t dockerserver . 
* sudo docker run -p 9090:9090 -p 9191:9191 dockerserver

### Test ###

* Web browser: locahost:9090  or localhost:9090/cat
* curl localhost:9090


