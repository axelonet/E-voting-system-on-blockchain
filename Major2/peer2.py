import socket
import jsonify as js

def send_votedata_to_peer(host,port,datalist):
    c = socket.socket()
    c.connect((host,port))
    try:
        data = js.jsonify_votedata(datalist)
        c.send(bytes(data,'utf-8'))
        if not c.recv(8192).decode()=='ACKD':
            raise ConnectionError

    except KeyboardInterrupt:
        pass


def broadcast_block(host,port,blockdata):
    pass
