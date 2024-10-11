# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/61517/python-dictionary-from-an-objects-fields
from l3.Runtime import _l_
def props(x):
    _l_(13405)

    aux = dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))
    _l_(13404)
    return aux

