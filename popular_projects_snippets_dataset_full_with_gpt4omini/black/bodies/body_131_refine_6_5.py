from enum import Enum # pragma: no cover

class Preview(Enum): # pragma: no cover
    string_processing = 'string_processing' # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.preview = False # pragma: no cover
        self.experimental_string_processing = True # pragma: no cover
 # pragma: no cover
feature = Preview.string_processing # pragma: no cover
self = MockSelf() # pragma: no cover

from enum import Enum # pragma: no cover

class Preview(Enum): # pragma: no cover
    string_processing = 'string_processing' # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.preview = False # pragma: no cover
        self.experimental_string_processing = True # pragma: no cover
 # pragma: no cover
feature = Preview.string_processing # pragma: no cover
self = MockSelf() # pragma: no cover
 # pragma: no cover
# Ensure exit functions are mocked to prevent termination in execution # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/mode.py
from l3.Runtime import _l_
"""
        Provide `Preview.FEATURE in Mode` syntax that mirrors the ``preview`` flag.

        The argument is not checked and features are not differentiated.
        They only exist to make development easier by clarifying intent.
        """
if feature is Preview.string_processing:
    _l_(6765)

    aux = self.preview or self.experimental_string_processing
    _l_(6764)
    exit(aux)
aux = self.preview
_l_(6766)
exit(aux)
