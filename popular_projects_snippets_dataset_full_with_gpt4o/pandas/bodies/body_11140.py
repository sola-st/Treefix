# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
df = DataFrame(
    {"key": ["a", "a", "a", "b", "b", "b"], "name": ["foo", "bar", "baz"] * 2}
)

result = df.groupby("key", group_keys=False).apply(lambda x: x)
tm.assert_frame_equal(result, df)
