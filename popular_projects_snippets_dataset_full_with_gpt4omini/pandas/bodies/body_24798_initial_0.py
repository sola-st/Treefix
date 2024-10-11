from typing import List # pragma: no cover

self = type('Mock', (), {})() # pragma: no cover
self._lines = [] # pragma: no cover
self.memory_usage_string = '100MB' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
from l3.Runtime import _l_
"""Add line containing memory usage."""
self._lines.append(f"memory usage: {self.memory_usage_string}")
_l_(10496)
