from typing import Callable, Any # pragma: no cover

class MockLeaf: value = 'Example quote: "Hello, world!"' # pragma: no cover
class MockSelf: normalize_strings = True # pragma: no cover
def normalize_string_quotes(input_string: str) -> str: return input_string.replace("'", '"') # pragma: no cover
self = MockSelf() # pragma: no cover
leaf = MockLeaf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
if self.normalize_strings:
    _l_(4485)

    leaf.value = normalize_string_quotes(leaf.value)
    _l_(4484)
