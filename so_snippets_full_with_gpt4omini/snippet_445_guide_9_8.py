class obj(object): # pragma: no cover
    def __init__(self, d): # pragma: no cover
        for k, v in d.items(): # pragma: no cover
            if isinstance(k, (list, tuple)): # pragma: no cover
                setattr(self, k[0], [obj(x) if isinstance(x, dict) else x for x in v]) # pragma: no cover
            else: # pragma: no cover
                setattr(self, k, obj(v) if isinstance(v, dict) else v) # pragma: no cover
d = {'a': 1, 'b': {'c': 2}, 'd': ['hi', {'foo': 'bar'}]} # pragma: no cover
x = obj(d) # pragma: no cover
foo_value = x.d[1]['foo'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1305532/how-to-convert-a-nested-python-dict-to-object
from l3.Runtime import _l_
class obj(object):
    _l_(1870)

    def __init__(self, d):
        _l_(1869)

        for k, v in d.items():
            _l_(1868)

            if isinstance(k, (list, tuple)):
                _l_(1867)

                setattr(self, k, [obj(x) if isinstance(x, dict) else x for x in v])
                _l_(1865)
            else:
                setattr(self, k, obj(v) if isinstance(v, dict) else v)
                _l_(1866)

d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
_l_(1871)
x = obj(d)
_l_(1872)
x.b.c
_l_(1873)
2
_l_(1874)
x.d[1].foo
_l_(1875)
'bar'
_l_(1876)

