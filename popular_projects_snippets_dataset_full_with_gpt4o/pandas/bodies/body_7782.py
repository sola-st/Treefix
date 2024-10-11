# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
rng = date_range("2009-01-01", "2010-01-01", freq=freq)
assert not rng.equals(list(rng))
