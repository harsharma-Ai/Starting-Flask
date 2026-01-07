from flask import Flask, render_template, request
from Moths.mathematics import summation, subtraction, multiplication, division

app = Flask(__name__)

@app.route('/sum')
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = summation(num1, num2)
    if result.is_integer():
        result = int(result)
        return str(result)
    
@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1, num2)
    if result.is_integer():
        result = int(result)
        return str(result)
    
@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiplication(num1, num2)
    if result.is_integer():
        result = int(result)
        return str(result)
    
@app.route("/div")
def div_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result =division(num1, num2)
    if result.is_integer():
        result = int(result)
        return str(result)
    else:
        return f"{result:.2f}"
       
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    