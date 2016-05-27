#!/usr/bin/python

import socket
import os
from src.cc import cc
import SimpleHTTPServer
import SocketServer


def server():
    # get server location
    host = socket.gethostname()
    port = int(cc.ask('What port on ' + host + ' shall we open?', 8085))

    path = cc.ask('What path shall we serve', '.')
    if path != '.':
        os.chdir(path)

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", port), Handler)

    print('Server running on port ' + str(port) + '!')
    httpd.serve_forever()

server()
