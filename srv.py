import socket
import sys
from src.cc import cc


def server():
    s = socket.socket()

    host = socket.gethostname()
    port = cc.ask('What port on ' + host + ' shall we open?', 22222)

    s.bind((host, port))
    s.listen(5)

    print("Listening on " + host + ":" + str(port))

    path = cc.persist('What file shall we serve?')


    while True:
        c, addr = s.accept()
        print('Got connection from', addr)

        # Re-open the file when the client connects
        f = open(path, 'r')
        l = f.read(1024)
        print('Opened file for sending')
        print('Sending file over')

        while l:
            sys.stdout.write('.')
            c.send(l)
            l = f.read(1024)

        c.close()
        print('')
        print('Kicked the client!')

        f.close()
        print('We sent the file ' + path + '!')

    s.close()
    print('Connection to server closed!')

try:
    server()
except KeyboardInterrupt:
    print('Goodbye!')
    exit(1)