obj = type('Mock', (object,), {'config': {'example_name': 42}})() # pragma: no cover
self = type('Mock', (object,), {'__name__': 'example_name', 'get_converter': lambda x: str(x)})() # pragma: no cover

obj = type('Mock', (object,), {'config': {'example_name': 'example_value'}})() # pragma: no cover
self = type('Mock', (object,), {'__name__': 'example_name', 'get_converter': lambda s, rv=None: s.upper()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
if obj is None:
    _l_(20148)

    aux = self
    _l_(20147)
    exit(aux)
rv = obj.config[self.__name__]
_l_(20149)
if self.get_converter is not None:
    _l_(20151)

    rv = self.get_converter(rv)
    _l_(20150)
aux = rv
_l_(20152)
exit(aux)
