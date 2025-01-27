# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH35439
idx = simple_index
expected = [str(x) for x in idx]
assert idx.format() == expected
