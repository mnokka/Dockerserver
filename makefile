# Author: mika.nokka1@gmail.com  January 2018:
#
# just build all
# usage: make -> build(everytime) and run 
# usage: make logs --> start flask server log following (use in different shell)
#
# Flask server uses sentenvs defined variables in code (-e parameter transfers as env into contaner)

# defines for the Host and Container (Flask server code)
HOSTDIR=~/tmp
CONTAINERDIR=/tmp
MOUNTDIR = $(HOSTDIR):$(CONTAINERDIR)
APPNAME = dockerserver
SHELLLOGFILE= flask.log
LOCAPORT=9090



default: run 

run: build
	sudo docker run -e CONTAINERDIR=$(CONTAINERDIR) -e SHELLLOGFILE=$(SHELLLOGFILE) -it -v $(MOUNTDIR) -p $(LOCAPORT):$(LOCAPORT) $(APPNAME) 
	
build: Dockerfile 
	sudo docker build -t $(APPNAME) . 


logs: 
	@echo "Starting logging of Flask server"
	sudo tail -f $(HOSTDIR)/$(SHELLLOGFILE)

.PHONY: run build logs setenvs
