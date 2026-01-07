from flask import Flask 
my_app = Flask("My first App") # app is just a reference name 

@my_app.route('/') # define the root and method that will be invoked when this root is accessed
# when u don't specify the request , by default, GET is requested

def home(): # home is a method, written as def home(): 
    return "Hello World"

if __name__ == "__main__": 
# add condition that web apps should run only if name attribute is set to main.
    my_app.run(debug=True)