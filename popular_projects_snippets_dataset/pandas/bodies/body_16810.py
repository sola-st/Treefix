# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
df = DataFrame(
    {"a": np.random.choice(["m", "f"], size=3), "b": np.random.randn(3)},
    index=tm.makeCustomIndex(3, 2),
)
df2 = DataFrame(
    {"a": np.random.choice(["m", "f"], size=10), "b": np.random.randn(10)}
)
msg = r'len\(right_on\) must equal the number of levels in the index of "left"'
with pytest.raises(ValueError, match=msg):
    merge(df, df2, right_on="b", left_index=True)
