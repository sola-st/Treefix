# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_ops.py
d = rng[10]

comp = rng > d
assert comp[11]
assert not comp[9]
