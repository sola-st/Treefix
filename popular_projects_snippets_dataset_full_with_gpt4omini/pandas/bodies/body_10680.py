# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_shift_diff.py
df = DataFrame(
    {"a": ["foo", "bar", "bar"], "b": ["baz", "foo", "foo"]}, dtype=object_dtype
)
with pytest.raises(TypeError, match=r"unsupported operand type\(s\) for -"):
    df.groupby("a")["b"].diff()
