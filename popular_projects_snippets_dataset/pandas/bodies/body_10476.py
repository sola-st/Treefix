# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_filters.py
# issue 11041
index = pd.MultiIndex.from_product([range(10), [0, 1]])
data = DataFrame(np.arange(100).reshape(-1, 20), columns=index, dtype="int64")
result = data.groupby(level=0, axis=1).filter(lambda x: x.iloc[0, 0] > 10)
expected = data.iloc[:, 12:20]
tm.assert_frame_equal(result, expected)
