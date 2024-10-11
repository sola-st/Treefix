# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
data = np.random.randn(5, 3)
other_data = np.random.randn(5, 3)
df = DataFrame(data)
other = DataFrame(other_data)
ndim_5 = np.ones(df.shape + (1, 3))

# DataFrame
assert df.eq(df).values.all()
assert not df.ne(df).values.any()
f = getattr(df, op)
o = getattr(operator, op)
# No NAs
tm.assert_frame_equal(f(other), o(df, other))
# Unaligned
part_o = other.loc[3:, 1:].copy()
rs = f(part_o)
xp = o(df, part_o.reindex(index=df.index, columns=df.columns))
tm.assert_frame_equal(rs, xp)
# ndarray
tm.assert_frame_equal(f(other.values), o(df, other.values))
# scalar
tm.assert_frame_equal(f(0), o(df, 0))
# NAs
msg = "Unable to coerce to Series/DataFrame"
tm.assert_frame_equal(f(np.nan), o(df, np.nan))
with pytest.raises(ValueError, match=msg):
    f(ndim_5)
