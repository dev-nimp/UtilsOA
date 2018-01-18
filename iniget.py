from configparser import ConfigParser
parser = ConfigParser()
#parser.read("conf.ini")
parser.read_file(open("conf.ini"))
parser['Server']['port']
#parser.getint('Server', 'port')
print(parser['Server']['port'])
