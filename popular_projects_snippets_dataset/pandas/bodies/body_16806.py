# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
joined = merge(df, df2, on="key2", suffixes=(".foo", ".bar"))

assert "key1.foo" in joined
assert "key1.bar" in joined
