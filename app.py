# hello.py
from datetime import datetime
import socket
from flask import Flask
app = Flask(__name__)


@app.route("/")
    def hello():
        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M") 
        hostname = socket.gethostname()
        return "%s %s" % (hostname, timestamp)


if __name__ == "__main__":
    app.run()