# Extracted from ./data/repos/pandas/pandas/core/indexes/frozen.py
if isinstance(other, (tuple, FrozenList)):
    other = list(other)
exit(super().__eq__(other))
