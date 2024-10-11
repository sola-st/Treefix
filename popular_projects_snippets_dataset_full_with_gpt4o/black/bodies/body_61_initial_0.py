class Mock: # pragma: no cover
    pass # pragma: no cover
self = Mock() # pragma: no cover
line_length = 80 # pragma: no cover
normalize_strings = True # pragma: no cover
self.line_length = line_length # pragma: no cover
self.normalize_strings = normalize_strings # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
self.line_length = line_length
_l_(18217)
self.normalize_strings = normalize_strings
_l_(18218)
