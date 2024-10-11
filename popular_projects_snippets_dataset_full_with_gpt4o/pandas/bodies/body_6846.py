# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# GH 19370
if isinstance(data, IntervalIndex):
    tuples = data.to_tuples()
else:
    tuples = [(iv.left, iv.right) if notna(iv) else iv for iv in data]
expected = IntervalIndex.from_tuples(tuples, closed=closed)
result = constructor(data, closed=closed)
tm.assert_index_equal(result, expected)
