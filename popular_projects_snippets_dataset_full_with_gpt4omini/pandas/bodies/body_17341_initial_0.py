from pandas import DataFrame # pragma: no cover

class MockGroupBy: # pragma: no cover
    def __init__(self, data): # pragma: no cover
        self.data = data # pragma: no cover
    def __getattr__(self, item): # pragma: no cover
        return self.data # pragma: no cover
    def groupby(self, *args, **kwargs): # pragma: no cover
        return self # pragma: no cover
obj = type('Mock', (object,), {'attrs': {'a': 1}, 'groupby': MockGroupBy([]).groupby})() # pragma: no cover
def method(gb): # pragma: no cover
    return gb # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/generic/test_finalize.py
from l3.Runtime import _l_
obj.attrs = {"a": 1}
_l_(8324)
result = method(obj.groupby([0, 0], group_keys=False))
_l_(8325)
assert result.attrs == {"a": 1}
_l_(8326)
