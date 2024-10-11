class MockBase(object): # pragma: no cover
    def __getitem__(self, key): # pragma: no cover
        return f'Value from key: {key}' # pragma: no cover
 # pragma: no cover
class MockClass(MockBase): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.accessed = False # pragma: no cover
 # pragma: no cover
    def test_method(self, key): # pragma: no cover
        aux = super().__getitem__(key) # pragma: no cover
 # pragma: no cover
builtins.exit = lambda x: print(f'Exiting with: {x}') # pragma: no cover
 # pragma: no cover
mock_obj = MockClass() # pragma: no cover
mock_obj.test_method('test') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(22619)
aux = super().__getitem__(key)
_l_(22620)
exit(aux)
