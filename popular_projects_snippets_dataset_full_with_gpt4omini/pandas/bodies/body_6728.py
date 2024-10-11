# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_formats.py
# GH 25984
index = IntervalIndex.from_tuples([(0, 1), np.nan, (2, 3)])
obj = constructor(list("abc"), index=index)
result = repr(obj)
assert result == expected
