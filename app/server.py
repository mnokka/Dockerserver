# Author mika.nokka1@gmail.com  January 2018
# https://github.com/mnokka/Dockerserver


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
		

@app.route('/test')
def hello_world():
    app.logger.warning ("--Just the test page-") #error goes to uWSGI console log too
    print("Printing: Test page section") # goes uWSGI console log
    return "Returning test page creation message\n"

@app.route('/cat')
def cat():
    app.logger.warning("--Cat section-") #error goes to uWSGI console log too
    print("==>Printing: Cat page section") # goes uWSGI console log
    return "Returning Cat page message: MIU\n"

@app.route('/sulo')
def sulo():
    app.logger.warning("--Cat named Sulo section-") #error goes to uWSGI console log too
    print("==> Printing: Cat named Sulo section") # goes uWSGI console log
    return "Cat named Sulo message returning\n"		
    
# @app.route('/', methods=['GET', 'POST']) #THIS WOULD MATCH ALL WEBHOOKS

    
        
    
# command=login
# parameter=user
# calling: /login?user=MYUSERNAME 
@app.route("/login", methods=["GET", "POST"])
def webhooklogin():
   
    
    if request.method == "GET":
    	app.logger.warning('Login command GET section')
    	print('Login command GET section')
        return "Login command GET section reporting back: OK"
    elif request.method == "POST": # FOR GITHUB EVENT WEBHOOK POST WITH DATA
        data = request.get_json() #(force=True)
        app.logger.warning( "--> Received data")
       
        user = request.args.get('user')
        app.logger.warning("--Login command initiated, user:{0} ".format(user)) #error goes to uWSGI console log too
    	print("==> Printing: Login command initiated, user:{0} ".format(user))  # goes uWSGI console log
        
        app.logger.warning('**********************************************')
        app.logger.warning('GOT JSON LOGIN Headers: %s', request.headers) 
        app.logger.warning('GOT JSON LOGIN Body: %s', request.get_data())
        app.logger.warning('**********************************************')

        print('**********************************************')
        print('GOT JSON LOGIN Headers: %s', request.headers) 
        print('GOT JSON LOGIN Body: %s', request.get_data())
        print('**********************************************')
          
    return "LOGIN command returning message"	
    
      
# command=command
# parameter1=param1
# parameter2=param2
# calling: /command?param1=kissa&param2=koira
@app.route("/command", methods=["GET", "POST"])
def webhookcommand():
   
    
    if request.method == "GET":
    	app.logger.warning('Command GET section')
    	print('Command GET section')
        return "Command GET section reporting back: OK"
    elif request.method == "POST": # FOR GITHUB EVENT WEBHOOK POST WITH DATA
        data = request.get_json() #(force=True)
        app.logger.warning( "--> Received data")
       
        param1 = request.args.get('param1')
        param2 = request.args.get('param2')
        
        
        app.logger.warning("-Command initiated, param1:{0} param2:{1}".format(param1,param2)) #error goes to uWSGI console log too
    	print("==> Printing: Command initiated, param1:{0} param2:{1}".format(param1,param2)) # goes uWSGI console log
        
        app.logger.warning('**********************************************')
        app.logger.warning('GOT JSON LOGIN Headers: %s', request.headers) 
        app.logger.warning('GOT JSON LOGIN Body: %s', request.get_data())
        app.logger.warning('**********************************************')

        print('**********************************************')
        print('GOT JSON LOGIN Headers: %s', request.headers) 
        print('GOT JSON LOGIN Body: %s', request.get_data())
        print('**********************************************')
          
    return "LOGIN command returning message"
    
    
	
if __name__ == "__main__":
	runtime="SERVER"
   	main(sys.argv[1:])
else:
	runtime="uWSGI"
	main(sys.argv[1:])