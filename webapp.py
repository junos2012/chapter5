#----Flask Hello World ----#
# Import the flask class from the flask module
from flask import Flask
from flask import render_template

#create the application object
webapp = Flask(__name__)

@webapp.route("/")	#use decorators to link the function to a url. decorators by default assume the methods require will be 'GET'
def index():
	return render_template("index.html")
#ensure there is a space between decorators and function to URL
@webapp.route("/about")
def about():
	return render_template("about.html")


#dynamic routes in your browser enter your username it should return your username on the page
@webapp.route("/user/<username>")
def user_profile(username):
	return "User {}".format(username)


#start the development server using the run() method
if __name__ == "__main__":
	webapp.run(debug=True)	
	#webapp.run(debug=True)
	#ensure you use (debug=True) if you seem to have a problem you can't find *DO NOT LEAVE THIS ON IN LIVE DEPLOYMENT*