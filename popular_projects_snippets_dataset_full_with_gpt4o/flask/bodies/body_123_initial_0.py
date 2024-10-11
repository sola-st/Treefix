class MockTemplate: # pragma: no cover
    def add_template_global(self, func, name=None): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
self = MockTemplate() # pragma: no cover
def f(): # pragma: no cover
    return 'Function f executed' # pragma: no cover
 # pragma: no cover
name = 'example_name' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
self.add_template_global(f, name=name)
_l_(22623)
aux = f
_l_(22624)
exit(aux)
