# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#38601
mi = MultiIndex.from_tuples([("A", 4), ("B", "3"), ("A", "2")])
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=mi)
obj = df.copy()
obj.loc[:, key] = np.zeros((2, 2), dtype="int64")
expected = DataFrame([[0, 2, 0], [0, 5, 0]], columns=mi)
tm.assert_frame_equal(obj, expected)

df = df.sort_index(axis=1)
df.loc[:, key] = np.zeros((2, 2), dtype="int64")
expected = expected.sort_index(axis=1)
tm.assert_frame_equal(df, expected)
