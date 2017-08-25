from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
	return "HELLOS THERE\n"

@app.route('/cat')
def cat():
    return "Cat says: MIU\n"

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
		
		
