import click # pragma: no cover

class MockBase(click.ParamType): # pragma: no cover
    def split_envvar_value(self, value): # pragma: no cover
        return value.split(',') # pragma: no cover
 # pragma: no cover
    def convert(self, value, param, ctx): # pragma: no cover
        return value.upper() # pragma: no cover
 # pragma: no cover
class MockDerived(MockBase): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.value = 'a,b,c' # pragma: no cover
 # pragma: no cover
    def split_envvar_value(self, value): # pragma: no cover
        return super().split_envvar_value(value) # pragma: no cover
 # pragma: no cover
    def convert(self, value, param, ctx): # pragma: no cover
        return super().convert(value, param, ctx) # pragma: no cover
 # pragma: no cover
mock_instance = MockDerived() # pragma: no cover
value = mock_instance.value # pragma: no cover
param = None # pragma: no cover
ctx = None # pragma: no cover
self = mock_instance # pragma: no cover
super_convert = mock_instance.convert # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
items = self.split_envvar_value(value)
_l_(22581)
super_convert = super().convert
_l_(22582)
aux = [super_convert(item, param, ctx) for item in items]
_l_(22583)
exit(aux)
