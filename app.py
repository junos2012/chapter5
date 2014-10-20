#flask work 

#import the flask module.
from flask import Flask

#create the application object
app = Flask(__name__)

#use decorators to link the function to a url 
@app.route("/")
def hello_world():
	return "Hello world??!?!?!?!?"

#dymanic route. 
@app.route("/test/<search_query>") #by default url's are string you can use converters though to change them to num's etc
def search(search_query):
	return search_query

@app.route("/float/<float:value>")
def float_url(value):
	print value + 1
	return "Correct"

@app.route("/float/<int:value>")
def int_url(value):
	print value + 1
	return "Correct"
#dynamic route which render's variable "name" but only returns 200 if name is equal to "owen"
@app.route("/user/<name>")
def user_page(name):
	if name.lower() == "owen":
		return "Hello {}".format(name), 200 #200 response is implied by default if not speficied best practice to define status code explicitly
	else:
		return "Not Found", 404




#run the application, *Never leave debug=True on with a live server.*
if __name__ == ("__main__"):
	app.run(debug=True)