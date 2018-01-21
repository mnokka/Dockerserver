# mika.nokka1@gmail.com -  Docker Build and Run January 2018
#

# defines
MOUNTDIR = ~/tmp:/tmp
LOCAPORT = 9090
APPNAME = dockerserver

default: run 

run: build
	sudo docker run -it -v $(MOUNTDIR) -p $(LOCAPORT):$(LOCAPORT) $(APPNAME)
	
build: Dockerfile
	sudo docker build -t $(APPNAME) . 
