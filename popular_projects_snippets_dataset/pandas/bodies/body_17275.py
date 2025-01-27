# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
df = pd.Series([1, 2], name="A", index=["a", "b"]).set_flags(
    allows_duplicate_labels=False
)
if frame:
    df = df.to_frame()
if isinstance(other, pd.Series) and frame:
    other = other.to_frame()
func = operator.methodcaller(func, other)
assert df.flags.allows_duplicate_labels is False
assert func(df).flags.allows_duplicate_labels is False
