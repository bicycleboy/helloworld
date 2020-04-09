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
    return "<h2>%s \"%s\" %s %s<h2>" % ("Hello good world from host ", hostname, " at ", timestamp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')