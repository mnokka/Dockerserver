from flask import Flask
import logging, sys
import logging.config
from logging import FileHandler
from logging.handlers import RotatingFileHandler


#logging works for uWSGI usage, not with pure flask server usage
#warning:ok
#critical:ok, message also to uWSGI console log
#debug: not working
#info: not working



app=Flask(__name__)

runtime="NA"
loglevel = logging.DEBUG  #just a comment deubg loggin not shown in logs (uWSGI mode)
logfile="/tmp/flask.log"

def main(argv):
	#logging.basicConfig(filename=logfile,level=loglevel) 
	print("Flask server logfile: {0}".format(logfile))
		
	
	handler = RotatingFileHandler(logfile, maxBytes=10000, backupCount=1)
	handler.setLevel(loglevel)
	
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
    print("Printing: CAT page section") # goes uWSGI console log
    return "Cat says: MIU\n"

		
		
if __name__ == "__main__":
	runtime="SERVER"
   	main(sys.argv[1:])
else:
	runtime="uWSGI"
	main(sys.argv[1:])