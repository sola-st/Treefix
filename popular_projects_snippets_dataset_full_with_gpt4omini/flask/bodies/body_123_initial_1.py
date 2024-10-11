from typing import Callable # pragma: no cover

class Mock: # pragma: no cover
    def add_template_global(self, f: Callable, name: str): pass # pragma: no cover
self = Mock() # pragma: no cover
f = lambda x: x * 2 # pragma: no cover
name = 'example_template' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
self.add_template_global(f, name=name)
_l_(5527)
aux = f
_l_(5528)
exit(aux)
