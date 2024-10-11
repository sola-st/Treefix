# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
df = DataFrame(
    np.random.randn(4, 3), index=[1, 10, "C", "E"], columns=[1, 2, 3]
)

result = df.iloc[:-1]
expected = df.loc[df.index[:-1]]
tm.assert_frame_equal(result, expected)

result = df.loc[[1, 10]]
expected = df.loc[Index([1, 10])]
tm.assert_frame_equal(result, expected)
