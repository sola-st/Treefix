# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# GH 6504, multi-axis indexing
df = DataFrame(
    np.random.randn(9, 2), index=[1, 1, 1, 2, 2, 2, 3, 3, 3], columns=["a", "b"]
)

expected = df.iloc[0:6]
result = df.loc[[1, 2]]
tm.assert_frame_equal(result, expected)

expected = df
result = df.loc[:, ["a", "b"]]
tm.assert_frame_equal(result, expected)

expected = df.iloc[0:6, :]
result = df.loc[[1, 2], ["a", "b"]]
tm.assert_frame_equal(result, expected)
