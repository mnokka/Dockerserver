from flask import Flask
import logging, sys
import logging.config
from logging import FileHandler

app=Flask(__name__)

loglevel = logging.INFO #just a comment
logfile="flask.log"

def main(argv):
	logging.basicConfig(filename=logfile,level=loglevel) 
	print("Flask server logfile: {0}".format(logfile))
	logging.info ("--Python starting Flask server--") 
	app.run(debug=True, host='0.0.0.0')
		

@app.route('/')
def hello_world():
    logging.info ("--Just the page-") 
    return "HELLOS THERE\n"

@app.route('/cat')
def cat():
    logging.info ("--CAT SECTIONS--")
    return "Cat says: MIU\n"

		
		
if __name__ == "__main__":
   main(sys.argv[1:])