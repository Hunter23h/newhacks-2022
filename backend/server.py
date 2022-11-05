from flask import Flask, request
from flask_cors import CORS, cross_origin

from citation import Citation
from summarizer import Summarizer
from reliability import Reliability


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/getdata", methods=["POST"])
@cross_origin()
def getdata():

    client_data = request.json
    summary_length = client_data['summarySize']
    print(client_data)

    url = client_data['link']
    citation = Citation(url).main() 
    summary = Summarizer(url, summary_length).main() 
    reliability = Reliability(url, Citation(url).date_finder()).main()

    return {
        "summary" : summary,
        "score" : reliability,
        "MLA" : citation
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
