o = 'test' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1303243/how-to-find-out-if-a-python-object-is-a-string
from l3.Runtime import _l_
def isStr(o):
    _l_(15277)

    aux = repr(o)[-1] in '\'"'
    _l_(15276)
    return aux

repr(o)[-1:].replace('"', "'") == "'"
_l_(15278)

