# Route decorators
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")

def home():
    return "Hello World!"

'''
@app.route("/userdetails/<userid>")
def getUserDetails(userid):
    return "User Details for  "+userid
'''

if __name__ == "__main__":
    app.run(debug=True)