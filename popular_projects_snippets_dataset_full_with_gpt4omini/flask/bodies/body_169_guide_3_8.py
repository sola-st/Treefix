class MyDict(dict): pass # pragma: no cover

self = MyDict() # pragma: no cover
self['key1'] = 'value1' # pragma: no cover
self['key2'] = 'value2' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
aux = f"<{type(self).__name__} {dict.__repr__(self)}>"
_l_(5543)
exit(aux)
