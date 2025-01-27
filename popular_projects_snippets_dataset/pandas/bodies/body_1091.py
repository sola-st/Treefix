# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
# GH#1534
mix = MultiIndex.from_tuples([("1a", "2a"), ("1a", "2b"), ("1a", "2c")])
df = DataFrame([[1, 2], [3, 4], [5, 6]], index=mix)
s = Series({(1, 1): 1, (1, 2): 2})
df["new"] = s
assert df["new"].isna().all()
