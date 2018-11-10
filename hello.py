"""Unix Processes

Usage:
	hello.py -m <message>


Options:
  -h --help     Show this screen.


"""
from docopt import docopt

def message(message):
	print(message)

if __name__ == '__main__':
    arguments = docopt(__doc__)

    # if an argument called hello was passed, execute the hello logic.
    if arguments['-m']:
      message(arguments['<message>'])