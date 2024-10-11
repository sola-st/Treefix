# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike.py
index = simple_index[:4]
result = index.isin(index)
assert result.all()

result = index.isin(list(index))
assert result.all()

result = index.isin([index[2], 5])
expected = np.array([False, False, True, False])
tm.assert_numpy_array_equal(result, expected)
