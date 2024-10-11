# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH#24924
key = np.array(0)

# dataframe __getitem__
df = DataFrame([[1, 2], [3, 4]])
result = df[key]
expected = Series([1, 3], name=0)
tm.assert_series_equal(result, expected)

# series __getitem__
ser = Series([1, 2])
result = ser[key]
assert result == 1
