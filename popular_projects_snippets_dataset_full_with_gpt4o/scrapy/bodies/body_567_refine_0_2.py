key = 'example_key' # pragma: no cover

class MockSuper:# pragma: no cover
    def __getitem__(self, item):# pragma: no cover
        return 'value_for_{}'.format(item)# pragma: no cover
# pragma: no cover
class Derived(MockSuper):# pragma: no cover
    def __getitem__(self, item):# pragma: no cover
        return super().__getitem__(item)# pragma: no cover
# pragma: no cover
key = 'example_key'# pragma: no cover
mock_object = Derived() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/datatypes.py
from l3.Runtime import _l_
try:
    _l_(20273)

    aux = super().__getitem__(key)
    _l_(20270)
    exit(aux)
except (TypeError, KeyError):
    _l_(20272)

    aux = None  # key is either not weak-referenceable or not cached
    _l_(20271)  # key is either not weak-referenceable or not cached
    exit(aux)  # key is either not weak-referenceable or not cached
