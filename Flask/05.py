# RENDERING TEMPLATES IN FLASK
from flask import Flask, render_template, request

app = Flask(__name__)  # Use __name__ for proper module resolution

@app.route('/sample/')
def get_sample_html():
    return render_template('sample.html')  # Make sure this file is in the 'templates' folder

@app.route('/user/<name>', methods=['GET'])
def greet_user(name):  # Match parameter name with route variable
    return render_template("result.html", username=name)

@app.route('/user', methods=['GET'])
def greet_user_based_on_req():
    user_name = request.args.get("username")  # Remove space from key
    return render_template("result.html", username=user_name)

if __name__ == "__main__":  # Correct entry point check
    app.run(debug=True, port=443)
    
    