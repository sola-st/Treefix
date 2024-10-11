self = type('Mock', (object,), {'normalize_strings': True})() # pragma: no cover
leaf = type('Mock', (object,), {'value': 'Example string'})() # pragma: no cover
def normalize_string_quotes(s): return s.replace('"', '\'').replace("'", "\'") # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
if self.normalize_strings:
    _l_(16236)

    leaf.value = normalize_string_quotes(leaf.value)
    _l_(16235)
