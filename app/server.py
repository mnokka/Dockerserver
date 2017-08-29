from flask import Flask
import logging, sys
import logging.config
from logging import FileHandler
from logging.handlers import RotatingFileHandler

app=Flask(__name__)

loglevel = logging.DEBUG  #just a comment
logfile="/tmp/flask.log"

def main(argv):
	#logging.basicConfig(filename=logfile,level=loglevel) 
	print("Flask server logfile: {0}".format(logfile))
	
	
	
	handler = RotatingFileHandler(logfile, maxBytes=10000, backupCount=1)
	handler.setLevel(loglevel)
	app.logger.addHandler(handler)
	
	logging.info ("--Python starting Flask server--") 
	#app.run(debug=False, host='0.0.0.0')
		

@app.route('/')
def hello_world():
    #logging.info ("--Just the page-") 
    app.logger.warning("--Just xxx the page-")
    return "HELLOS THERE\n"

@app.route('/cat')
def cat():
    #logging.info ("--CAT SECTIONS--")
    app.logger.error("--CAT MIUS-")
    return "Cat says: MIU\n"

		
		
if __name__ == "__main__":
   main(sys.argv[1:])
else:
	print("ARGH")
	main(sys.argv[1:])