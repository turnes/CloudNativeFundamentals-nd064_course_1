import logging
from flask import Flask, json
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("--> default flask logger <-- /")
    logger.info("/")
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info("--> default flask logger <-- Status")
    logger.info("Status")
    return jsonify(result="OK - healthy")

@app.route("/metrics")
def metrics():
    r = app.response_class(
        response = json.dumps({
            "status":"success",
            "code":0,
            "data":{
                "UserCount":140,
                "UserCountActive":23
            }
            }
        ),
        status=200,
        mimetype="application/json"
    )
    app.logger.info("--> default flask logger <-- Metrics")
    logger.info("Metrics")
    return r

if __name__ == "__main__":
    # default log
    logging.basicConfig(filename='app.log',level=logging.INFO)
    # custom log  
    formatter = logging.Formatter('%(asctime)s, %(message)s endpoint was reached.', datefmt="%m/%d/%Y %I:%M:%S %p %Z")
    handler = logging.FileHandler(filename='app.log')
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    logger = logging.getLogger('status')    
    logger.addHandler(handler)
    logger.propagate = False

                
    app.run(host='0.0.0.0')
