# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike.py
index = simple_index
assert index.freq is not None

result = index[:]
assert result.freq == index.freq
