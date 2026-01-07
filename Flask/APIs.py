from flask import Flask, request

app = Flask(__name__)

""" 
>> Here, are some example of parameters types in FLASK.
1. String: "/user/<username>" or Any string - captures a string parameter.
2. Integer: "/post/<int:post_id> or "/person/<int:age_min>" - captures an integer parameter.
3. Float: "/price/<float:price>" or "/person/<float:height_max>" - captures a float parameter.
4. Path: "/path/<path:subpath>" or "/main/test/sub[slashes ar expected]" - captures a path parameter, including slashes.
5. UUID: "/item/<uuid:item_id>" or "/network/<uuid:uuid>" - captures a UUID parameter.
"""
@app.route("/book/<isbn>")
def get_author():
    res = request.get("https://openlibrary.org/isbn/{escape(isbn)}.json")
    if res.status_code == 200:
        return {"message": res.json()}
    elif res.status_code == 404:
        return {"message": "Something Went Wrong"}, 404
    else:
        return {"message": "Server ERROR!"}, 500
    
if __name__ == "__main__":
   app.run(debug=True)
# Run the Flask application

# Example of the UUID are:

"""
>>  @app.route("/network/<uuid:uuid>")
    def get_network(uuid):
        res = request.get("https://anotherapi/getnetwork/{uuid}.json")
        if res.status_code == 200:
            return {"message": res.json()}
        elif res.status_code == 404:
            return {"message": "Network Not Found"}
        else:
            return {"message": "Something went wrong"}
    if __name__ == "__main__":
        app.run(debug=True)
            
"""
    
"""

# JSON HTTP RETURN Status Coders ->

    >>  Code      Description
       1. 200    : Request Successful.
       2. 201    : New Resource Created.
       3. 204    : Request accepted, but in process.
       4. 400    : Bad/Invalid Request.
       5. 401    : Unauthorized, Authentication or Credentials missing.
       6. 403    : Credentials not sufficient to access the resource.
       7. 404    : Resource Not Found.
       8. 500    : Internal/Unexpected Server Error.
       9. 502    : Bad Gateway.
       10. 503   : Service Unavailable.
       11. 504   : Gateway Timeout.
       12. 511   : Network Authentication Required.
       
"""
# we can change the port also by adding port=500 in app.run function.
    