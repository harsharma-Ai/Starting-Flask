from flask import Flask
app = Flask(__name__)

@app.errorhandler(404)
def api_not_found(error):
    # This function is a custom error handler for 404 Not Found errors
    # It is triggered whenever a 404 error occurs within the Flask application
    return {"message": "API not found"}, 404

@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500

@app.route("/test500")
def test500():
    raise Exception("Forced exception for testing")

if __name__ == "__main__":
    app.run(debug=True)