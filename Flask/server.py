from flask import Flask

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    # Return a simple string as the response
    return "<b>My first Flask application in action!</b>"
if __name__ == "__main__":
    app.run(debug=True)
    # we can change the port also by adding port=500 in app.run function.