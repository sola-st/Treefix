# Extracted from ./data/repos/pandas/pandas/core/indexes/frozen.py
if isinstance(other, tuple):
    other = list(other)
exit(type(self)(other + list(self)))
