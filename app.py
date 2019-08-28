import sys

import itchat
from pygtail import Pygtail

TONAME = '大发明家'

def send(username):
    for line in Pygtail('msg.log'):
        itchat.send(line, toUserName=username)
        sys.stdout.write(line)


def main():
    itchat.auto_login()
    try:
        username = itchat.search_friends(name=TONAME)[0]['UserName']
    except:
        sys.stdout.write('未找到指定用户')
        sys.exit()


    while True:
        send(username)

if __name__ == '__main__':
    main()
