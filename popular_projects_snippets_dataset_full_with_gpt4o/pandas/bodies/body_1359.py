# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#17192 iloc with read-only array raising TypeError
df = DataFrame({"data": np.ones(100, dtype="float64")})
indices = np.array([1, 3, 6])
indices.flags.writeable = False

result = df.iloc[indices]
expected = df.loc[[1, 3, 6]]
tm.assert_frame_equal(result, expected)

result = df["data"].iloc[indices]
expected = df["data"].loc[[1, 3, 6]]
tm.assert_series_equal(result, expected)
