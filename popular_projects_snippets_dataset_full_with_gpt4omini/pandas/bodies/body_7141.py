# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH35439
idx = simple_index
max_width = max(len(str(x)) for x in idx)
expected = [str(x).ljust(max_width) for x in idx]
assert idx.format() == expected
