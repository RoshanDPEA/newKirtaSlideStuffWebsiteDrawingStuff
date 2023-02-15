from time import sleep

firstline = ' '


def write(streng):
    log = open('log.txt', 'w')
    log.truncate(0)
    log.close()
    log = open('log.txt', 'a')
    log.write(str(streng))
    log.close()

def refresh():
    with open("log.txt") as f:
        lines = f.read()
        global firstline
        firstline = lines.split('\n', 1)[0]

def getline():
    return firstline
