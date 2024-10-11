# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# complex
arr = np.array([np.nan, 1, 6, np.nan])
arr2 = np.array([2j, np.nan, 7, None])
df = DataFrame({"a": arr})
df2 = DataFrame({"a": arr2})

msg = "|".join(
    [
        "'>' not supported between instances of '.*' and 'complex'",
        r"unorderable types: .*complex\(\)",  # PY35
    ]
)
with pytest.raises(TypeError, match=msg):
    # inequalities are not well-defined for complex numbers
    df.gt(df2)
with pytest.raises(TypeError, match=msg):
    # regression test that we get the same behavior for Series
    df["a"].gt(df2["a"])
with pytest.raises(TypeError, match=msg):
    # Check that we match numpy behavior here
    df.values > df2.values

rs = df.ne(df2)
assert rs.values.all()

arr3 = np.array([2j, np.nan, None])
df3 = DataFrame({"a": arr3})

with pytest.raises(TypeError, match=msg):
    # inequalities are not well-defined for complex numbers
    df3.gt(2j)
with pytest.raises(TypeError, match=msg):
    # regression test that we get the same behavior for Series
    df3["a"].gt(2j)
with pytest.raises(TypeError, match=msg):
    # Check that we match numpy behavior here
    df3.values > 2j
