from flask import Flask
import logging
app = Flask(__name__)
logging.basicConfig(filename='flask.log', level=logging.INFO)
@app.route('/')
def hello_world():
    return 'rajesh'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
