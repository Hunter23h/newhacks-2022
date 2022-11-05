from flask import Flask
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/getdata", methods=["POST" ,"GET"])
@cross_origin()
def getdata():
    return {"Message" : "it works yay"}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
