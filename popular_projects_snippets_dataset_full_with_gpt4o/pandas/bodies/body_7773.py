# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_equals.py

assert not index.equals(Index(index.asi8))
assert not index.equals(Index(index.asi8.astype("u8")))
assert not index.equals(Index(index.asi8).astype("f8"))
