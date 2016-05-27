import mechanize
import socket
from subprocess import call
from src.cc import cc
import os


def download_link(br, l):
    # f = open(l.text, "w")  # perhaps you should open in a better way & ensure that file doesn't already exist.
    br.click_link(l)
    # f.write(br.response().read())
    print(l.text, " has been downloaded")
    # br.back()


def grab():
    # Make a Browser (think of this as chrome or firefox etc)
    br = mechanize.Browser()

    # Open your site
    host = cc.ask('What host shall we fetch the file from?', socket.gethostname())
    port = int(cc.ask('What port on ' + host + ' shall we listen to?', 8085))

    site = 'http://' + host + ':' + str(port)
    br.open(site)

    myfiles = []
    index = 0
    for l in br.links():  # You can also iterate through br.forms() to print forms on the page!
        index += 1
        print(str(index) + ":\t" + l.text)
        myfiles.append(l)

    path = cc.ask('Set download location', '.')
    if not os.path.exists(path):
        print('Creating ' + path)
        os.makedirs(path)

    if (str(cc.ask('Download all files (y/N)?', 'N')).capitalize() == 'Y'):
        cmd = "wget -r -e robots=off -nH --directory-prefix=\"" + path + "\" --reject \"index.html*\" " + site
        print('Executing ' + cmd)
        call(cmd, shell=True)
    else:
        menu_item = int(cc.persist('Which file do you want to download (1 to ' + str(index) + ')?')) - 1
        if 0 <= menu_item < len(myfiles):
            print('Downloading ' + myfiles[menu_item].text)
        else:
            print("Can't find that one! :/")

        print('Goodbye!')


grab()
