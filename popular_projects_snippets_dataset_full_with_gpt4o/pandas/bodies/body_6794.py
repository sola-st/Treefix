# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH 25860
index = IntervalIndex.from_arrays(values[1:], values[:-1])
result = index.get_loc(index[0])
expected = 0
assert result == expected
