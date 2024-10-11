self = type('Mock', (object,), {})() # pragma: no cover
self._lines = [] # pragma: no cover
self.memory_usage_string = '1024 MB' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
from l3.Runtime import _l_
"""Add line containing memory usage."""
self._lines.append(f"memory usage: {self.memory_usage_string}")
_l_(21668)
