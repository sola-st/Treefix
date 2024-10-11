# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py

df = DataFrame(np.random.randn(4, 10), columns=range(0, 20, 2))

result = df.iloc[:, 1]
exp = df.loc[:, 2]
tm.assert_series_equal(result, exp)

result = df.iloc[:, 2]
exp = df.loc[:, 4]
tm.assert_series_equal(result, exp)

# slice
result = df.iloc[:, slice(4, 8)]
expected = df.loc[:, 8:14]
tm.assert_frame_equal(result, expected)

# list of integers
result = df.iloc[:, [1, 2, 4, 6]]
expected = df.reindex(columns=df.columns[[1, 2, 4, 6]])
tm.assert_frame_equal(result, expected)
