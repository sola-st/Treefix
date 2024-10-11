class Mock(object): pass # pragma: no cover
self = Mock() # pragma: no cover
serializer = 'example_serializer' # pragma: no cover
self.serializer = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
"""Create a tagger for the given serializer."""
self.serializer = serializer
_l_(17703)
