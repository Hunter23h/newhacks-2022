from flask import Flask, request
from flask_cors import CORS, cross_origin
from citation import Citation
from summarizer import Summarizer


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/getdata", methods=["POST"])
@cross_origin()
def getdata():

    client_data = request.json
    print(client_data)

    url = client_data['link']
    citation = Citation(url).main() 
    summary = Summarizer(url).main() 

    return {
        "summary" : summary,
        "score" : 5,
        "MLA" : citation
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
