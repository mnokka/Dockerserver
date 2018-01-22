# README #


### What is this repository for? ###

* Running Flask server +  using application server uwsgi inside docker image
* Tested Virtual box + Ubuntu 16.4 LTS (Host Windows10 + VirtualBox)
* Tested Minut 17.2
* Flask logging works under uWSGI
* Pure flask server rans, but logging not working


### How do I get set up? ###

* Install Docker   https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-repository
* Do not use Ambientia VPN

* Clone repo and execute in root
* sudo docker build -t dockerserver . 
* sudo docker run -it -v ~/tmp:/tmp -p 9090:9090 dockerserver
* Or just execute makefile to build and start server in container: make

* Log (in host): ~/tmp/flask.log, uWSGI logs to console 
* Or just tart following server logs: make logs

* Flask server runtime variables defined in makefile (mount definitions, default localhost ports)

### Test ###

* Web browser: locahost:9090  or localhost:9090/cat or localhost:9090/sulo
* curl localhost:9090 or curl localhost:9090/cat or curl localhost:9090/cat 


