from collections import UserDict # pragma: no cover

key = 'example_key' # pragma: no cover
def_val = ['default_value'] # pragma: no cover
class MockDict(UserDict):# pragma: no cover
    def get(self, key, default):# pragma: no cover
        return self.data.get(key, default)# pragma: no cover
# pragma: no cover
mock_dict = MockDict({'example_key': ['value1', 'value2']})# pragma: no cover
super = lambda: mock_dict # pragma: no cover

from collections import UserDict # pragma: no cover

key = 'example_key' # pragma: no cover
def_val = ['default_value'] # pragma: no cover
class MockDict(UserDict):# pragma: no cover
    def __init__(self, initial_data=None):# pragma: no cover
        super().__init__(initial_data)# pragma: no cover
# pragma: no cover
mock_dict = MockDict({'example_key': ['value1', 'value2']}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
try:
    _l_(6763)

    aux = super().get(key, def_val)[-1]
    _l_(6760)
    exit(aux)
except IndexError:
    _l_(6762)

    aux = None
    _l_(6761)
    exit(aux)
