import sys # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
from l3.Runtime import _l_
try:
    import types
    _l_(15223)

except ImportError:
    pass

def func(_static=types.SimpleNamespace(counter=0)):
    _l_(15226)

    _static.counter += 1
    _l_(15224)
    print(_static.counter)
    _l_(15225)

