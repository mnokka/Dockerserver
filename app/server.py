# Author mika.nokka1@gmail.com  January 2018
#


from flask import Flask
import logging, sys
import logging.config
from logging import FileHandler
from logging.handlers import RotatingFileHandler
from logging import Formatter
import os
from flask import request # for parameter handling


#logging works for uWSGI usage, not with pure flask server usage
#warning:ok
#critical:ok, message also to uWSGI console log
#debug: not working
#info: not working



app=Flask(__name__)

runtime="NA"
loglevel = logging.DEBUG  #just a comment deubg loggin not shown in logs (uWSGI mode)
#logfile="/tmp/flask.log"
user="NA"
pwd="NA"

def main(argv):
	#logging.basicConfig(filename=logfile,level=loglevel) 
	
	shellvar1=os.environ['SHELLLOGFILE']
	shellvar2=os.environ['CONTAINERDIR']
	print ("===> Using shell variable SHELLLOGFILE:{0}".format(shellvar1))
	print ("===> Using shell variable CONTAINERDIR:{0}".format(shellvar2))	
	logfile=shellvar2+"/"+shellvar1
	print("===> Host Flask server logfile: {0}".format(logfile))
	
	handler = RotatingFileHandler(logfile, maxBytes=10000, backupCount=1)
	handler.setLevel(loglevel)
	handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s '))
	
	app.logger.addHandler(handler)
	
	if (runtime=="SERVER"): 
		app.logger.warning  ("--Python starting standalone Flask server--") 
		app.run(debug=False, host='0.0.0.0')
	if (runtime=="uWSGI"):
		app.logger.warning ("-- uWSGI running Flask server--") #goes uWSGI console
		

@app.route('/')
def hello_world():
    app.logger.warning ("--Just xxx the page-") #error goes to uWSGI console log too
    print("Printing: xxxx page section") # goes uWSGI console log
    return "HELLOS THERE\n"

@app.route('/cat')
def cat():
    app.logger.warning("--CAT MIUS SECTION-") #error goes to uWSGI console log too
    print("==>Printing: CAT page section") # goes uWSGI console log
    return "Cat says: MIU\n"

@app.route('/sulo')
def sulo():
    app.logger.warning("--CAT IS Sulo SECTION-") #error goes to uWSGI console log too
    print("==> Printing: CAT is Sulo") # goes uWSGI console log
    return "Cat is Sulo and says: MIU-MAU\n"		
    
# This is an example. Please do not send passwords really like here
# Calling localhost:9090/login?user=sulo&pwd=maumau
@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('user')
    password = request.args.get('pwd')
    app.logger.warning("--Login initiated, user:{0} passwd:{1}".format(username,password)) #error goes to uWSGI console log too
    print("==> Printing: Login initiated, user:{0} passwd:{1}".format(username,password)) # goes uWSGI console log
    message=("<b>Login initiated for user:{0}  (password is:{1}</b>)".format(username,password))
    return message

	
if __name__ == "__main__":
	runtime="SERVER"
   	main(sys.argv[1:])
else:
	runtime="uWSGI"
	main(sys.argv[1:])