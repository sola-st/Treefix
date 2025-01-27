# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
joined = merge(
    df,
    df2,
    left_on="key2",
    right_on="key1",
    suffixes=(".foo", ".bar"),
)
assert "key1.foo" in joined
assert "key2.bar" in joined
