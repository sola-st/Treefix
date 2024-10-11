# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
df = DataFrame(
    {"a": np.random.choice(["m", "f"], size=3), "b": np.random.randn(3)}
)
df2 = DataFrame(
    {"a": np.random.choice(["m", "f"], size=10), "b": np.random.randn(10)},
    index=tm.makeCustomIndex(10, 2),
)
msg = r"len\(right_on\) must equal len\(left_on\)"
with pytest.raises(ValueError, match=msg):
    merge(df, df2, right_on="a", left_on=["a", "b"])
