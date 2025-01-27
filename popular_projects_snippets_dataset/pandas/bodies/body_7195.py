# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
# GH#44609 case where we have to upcast
idx = NumericIndex(np.array([1, 2, 3], dtype=np.int8))
result = idx.map(lambda x: x * 1000)
# TODO: we could plausibly try to infer down to int16 here
expected = NumericIndex([1000, 2000, 3000], dtype=np.int64)
tm.assert_index_equal(result, expected)
