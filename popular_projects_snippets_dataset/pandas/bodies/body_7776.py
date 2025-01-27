# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_equals.py

other = Index([str(x) for x in index], dtype=object)
assert not index.equals(other)
assert not index.equals(CategoricalIndex(other))
