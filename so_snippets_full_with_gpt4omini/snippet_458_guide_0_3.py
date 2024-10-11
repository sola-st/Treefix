import platform # pragma: no cover

platform = type('Mock', (object,), {'python_version': lambda: '3.8.5'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/954834/how-do-i-use-raw-input-in-python-3
from l3.Runtime import _l_
try:
    import platform
    _l_(588)

except ImportError:
    pass
def str_input(str=''):
    _l_(594)

    py_version = platform.python_version() # fetch the python version currently in use
    _l_(589) # fetch the python version currently in use
    if int(py_version[0]) == 2:
        _l_(591)

        aux = raw_input(str) # input string in python2
        _l_(590) # input string in python2
        return aux # input string in python2
    if int(py_version[0]) == 3:
        _l_(593)

        aux = input(str) # input string in python3
        _l_(592) # input string in python3
        return aux # input string in python3

str_input("Your Name: ")
_l_(595)

