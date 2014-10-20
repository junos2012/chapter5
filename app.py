#flask work 

#import the flask module.
from flask import Flask

#create the application object
app = Flask(__name__)

#use decorators to link the function to a url 
@app.route("/")
def hello_world():
	return "Hello world"

#run the application, *Never leave debug=True on with a live server.*
if __name__ == ("__main__"):
	app.run(debug=True)