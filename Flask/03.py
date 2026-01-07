from flask import Flask, request
app = Flask(__name__)
@app.route("/person", methods=['POST'])
def add_by_uuid():
    new_person = request.json
    if not new_person:
        return {"message": "Invalid input parameter"}, 422
    # code to validate new_person ommited
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500

    return {"message": f"{new_person['id']}"}, 200
if __name__ == "__main__":
    app.run(debug=True, port= 500)
    
# we can change the port also by adding port=500 in app.run function.