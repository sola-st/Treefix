# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
other = Index(list("abc"))
assert not index.equals(other)
