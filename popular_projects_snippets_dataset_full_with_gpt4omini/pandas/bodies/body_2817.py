# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
df = DataFrame(np.random.randn(10, 4))

# axis=0
result = df.reindex(list(range(15)))
assert np.isnan(result.values[-5:]).all()

result = df.reindex(range(15), fill_value=0)
expected = df.reindex(range(15)).fillna(0)
tm.assert_frame_equal(result, expected)

# axis=1
result = df.reindex(columns=range(5), fill_value=0.0)
expected = df.copy()
expected[4] = 0.0
tm.assert_frame_equal(result, expected)

result = df.reindex(columns=range(5), fill_value=0)
expected = df.copy()
expected[4] = 0
tm.assert_frame_equal(result, expected)

result = df.reindex(columns=range(5), fill_value="foo")
expected = df.copy()
expected[4] = "foo"
tm.assert_frame_equal(result, expected)

# other dtypes
df["foo"] = "foo"
result = df.reindex(range(15), fill_value=0)
expected = df.reindex(range(15)).fillna(0)
tm.assert_frame_equal(result, expected)
