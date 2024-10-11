from typing import List # pragma: no cover

self = type('Mock', (object,), {'_items': []})() # pragma: no cover
index = 0 # pragma: no cover
item = 'sample_item' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
from l3.Runtime import _l_
self._items.insert(index, item)
_l_(18509)
