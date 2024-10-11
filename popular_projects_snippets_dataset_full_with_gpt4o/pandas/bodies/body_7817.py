# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike.py
idx = simple_index
idx = idx.insert(1, pd.NaT)

result = idx.argsort()
expected = idx._data.argsort()
tm.assert_numpy_array_equal(result, expected)
