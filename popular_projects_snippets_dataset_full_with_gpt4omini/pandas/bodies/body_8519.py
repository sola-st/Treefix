# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# GH#9512
idx = DatetimeIndex(vals)
assert idx[0] in idx
