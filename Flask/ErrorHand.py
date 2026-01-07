# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
      return "hello world"
    
if __name__ == "__main__":
  app.run(debug=True)
"""
-> 404 NOT FOUND
-> 500 INTERNAL SERVER ERROR

Write routes to process requests to the Falsk server at specific URLs.
Handle parameters and arguments sent to the URLs.
Write error handlers for server and user errors.
"""
# we can change the port also by adding port=500 in app.run function.