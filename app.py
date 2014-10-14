#----Flask Hello World ----#
# Import the flask class from the flask module
from flask import Flask

#create the application object
webapp = Flask(__name__)

@webapp.route("/")	#use decorators to link the function to a url
def index():
	return """
	This is the index page or ROOT of your webserver,
	rather than returning this text you could import from flask
	"render_template", and use an actual html index.html page ;).
	this is how you do it ;)

	"""


#dynamic route


#start the development server using the run() method
if __name__ == "__main__":
	webapp.run()