d = {'a': 1, ('d',): ['hi', {'foo': 'bar'}]} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1305532/how-to-convert-a-nested-python-dict-to-object
from l3.Runtime import _l_
class obj(object):
    _l_(14018)

    def __init__(self, d):
        _l_(14017)

        for k, v in d.items():
            _l_(14016)

            if isinstance(k, (list, tuple)):
                _l_(14015)

                setattr(self, k, [obj(x) if isinstance(x, dict) else x for x in v])
                _l_(14013)
            else:
                setattr(self, k, obj(v) if isinstance(v, dict) else v)
                _l_(14014)

d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
_l_(14019)
x = obj(d)
_l_(14020)
x.b.c
_l_(14021)
2
_l_(14022)
x.d[1].foo
_l_(14023)
'bar'
_l_(14024)

