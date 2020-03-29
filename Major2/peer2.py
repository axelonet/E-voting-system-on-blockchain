import socket
import jsonify as js
import pickle as pk

def connect_to_peer(host,port,datalist):
    c = socket.socket()
    c.connect((host,port))
    try:
        data = pk._dumps(datalist)
        c.send(bytes(data))
        if not c.recv(1024).decode()=='ACKD':
            raise ConnectionError

    except KeyboardInterrupt:
        pass
