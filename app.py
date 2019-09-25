# hello.py
from datetime import datetime
import socket
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S") 
    hostname = socket.gethostname()
    return "$%s %s %s %s" % ("Hello world from ", hostname, " at ", timestamp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')