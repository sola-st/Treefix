class Preview(type('Mock', (object,), {})): # pragma: no cover
    string_processing = "string_processing" # pragma: no cover
 # pragma: no cover
class MockSelf(type('Mock', (object,), {})): # pragma: no cover
    preview = False # pragma: no cover
    experimental_string_processing = False # pragma: no cover
 # pragma: no cover
feature = Preview.string_processing # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/mode.py
from l3.Runtime import _l_
"""
        Provide `Preview.FEATURE in Mode` syntax that mirrors the ``preview`` flag.

        The argument is not checked and features are not differentiated.
        They only exist to make development easier by clarifying intent.
        """
if feature is Preview.string_processing:
    _l_(18456)

    aux = self.preview or self.experimental_string_processing
    _l_(18455)
    exit(aux)
aux = self.preview
_l_(18457)
exit(aux)
