# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# #1201
df = DataFrame(np.random.randn(5, 3), index=["foo", "foo", "bar", "baz", "bar"])

result = df.loc["foo"]
expected = df[:2]
tm.assert_frame_equal(result, expected)

result = df.loc["bar"]
expected = df.iloc[[2, 4]]
tm.assert_frame_equal(result, expected)

result = df.loc["baz"]
expected = df.iloc[3]
tm.assert_series_equal(result, expected)
