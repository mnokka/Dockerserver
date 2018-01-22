# README #


### What is this repository for? ###

* Running Flask server +  using application server uwsgi inside docker image
* Tested 1) Window 10 Virtual box + Ubuntu 16.4 LTS   2) Standalone Mint 17.2
* Flask logging works under uWSGI
* Pure flask server rans, but logging not working (code detects "runtime env")


### How do I get set up? ###

* Install Docker   https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-repository
* Do not use Ambientia VPN
MANUALLY
	* Clone repo and execute in root
	* sudo docker build -t dockerserver . 
	* sudo docker run -it -v ~/tmp:/tmp -p 9090:9090 dockerserver
VIA MAKE
* Or just execute makefile to build and start server in container: make
LOGS
* uWSGI logs goes to start console 
* Log (in host): ~/tmp/flask.log 
* Or just start following server logs (from host): make logs

* Flask server runtime variables are defined in makefile (mount definitions host-container, default port, application name)

### Test ###

* Web browser: locahost:9090  or localhost:9090/cat or localhost:9090/sulo
* curl localhost:9090 or curl localhost:9090/cat or curl localhost:9090/cat 
* Web browser: localhost:9090/login?user=MYUSERNAME&pwd=MYPASSWORD  THIS IS JUST EXAMPLE TO PARSE PARAMETERS...


