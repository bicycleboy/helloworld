# hello.py
from datetime import datetime
import socket
now = datetime.now()
timestamp = now.strftime("%d/%m/%Y %H:%M") 
hostname = socket.gethostname()
print(hostname, timestamp)
