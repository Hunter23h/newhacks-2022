from flask import Flask, request
from flask_cors import CORS, cross_origin

from citation import Citation
from summarizer import Summarizer
from reliability import Reliability

app = Flask(__name__, static_url_path="", static_folder='./build', template_folder='build')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["GET"])
def frontend():
    return app.send_static_file('index.html')


@app.route("/getdata", methods=["POST"])
@cross_origin()
def getdata():

    client_data = request.json
    summary_length = client_data['summarySize']
    print(client_data)

    url = client_data['link']

    try:
        citation = Citation(url).main() 
    except:
        citation = "Citation not available"
    
    try:
        summary = Summarizer(url, summary_length).main() 
    except:
        summary = "Summary not available :("

    reliability = Reliability(url, Citation(url).date_finder()).main() 

    return {
        "summary" : summary,
        "score" : reliability,
        "MLA" : citation
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
