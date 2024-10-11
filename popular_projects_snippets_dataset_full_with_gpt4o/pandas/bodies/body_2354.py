# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
df = multiindex_dataframe_random_data
result = df.xs("two", level="second")
expected = df[df.index.get_level_values(1) == "two"]
expected.index = Index(["foo", "bar", "baz", "qux"], name="first")
tm.assert_frame_equal(result, expected)
