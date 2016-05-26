import socket
import sys

from src.cc import cc


def client():
    s = socket.socket()

    host = cc.ask('What host shall we fetch the file from?', socket.gethostname())
    port = int(cc.ask('What port on ' + host + ' shall we listen to?', 22222))

    s.connect((host, port))

    cc.say("Connected to " + host + ":" + str(port))

    path = cc.persist('Save file as which path?')

    with open(path, 'w+') as f:
        cc.say("We've created the file " + path + " :)")
        cc.say('Receiving data')
        while True:
            sys.stdout.write('.')
            data = s.recv(1024)
            if not data:
                break

            # Write data to a file
            f.write(data)

        # Newline
        print('')
        f.close()
        cc.say('We got the file!')

    s.close()
    cc.say('Connection to server closed!')


client()
