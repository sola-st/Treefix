# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
from l3.Runtime import _l_
try:
    import types
    _l_(3236)

except ImportError:
    pass

def func(_static=types.SimpleNamespace(counter=0)):
    _l_(3239)

    _static.counter += 1
    _l_(3237)
    print(_static.counter)
    _l_(3238)

