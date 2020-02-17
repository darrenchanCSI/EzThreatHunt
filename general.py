from datetime import datetime
from IPython.display import clear_output
from IPython import get_ipython
from os import system, name

def getTimestamp():
    return "[" + datetime.now().strftime("%H:%M:%S") + "] "

def clear():
    if get_ipython():
        _ = clear_output()
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
