# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_datetimelike.py
# GH35439
idx = simple_index
expected = [f"{x:%Y-%m-%d}" for x in idx]
assert idx.format() == expected
