# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_align.py
af, bf = float_frame.align(float_frame)
assert af._mgr is not float_frame._mgr

af, bf = float_frame.align(float_frame, copy=False)
assert af._mgr is float_frame._mgr

# axis = 0
other = float_frame.iloc[:-5, :3]
af, bf = float_frame.align(other, axis=0, fill_value=-1)

tm.assert_index_equal(bf.columns, other.columns)

# test fill value
join_idx = float_frame.index.join(other.index)
diff_a = float_frame.index.difference(join_idx)
diff_a_vals = af.reindex(diff_a).values
assert (diff_a_vals == -1).all()

af, bf = float_frame.align(other, join="right", axis=0)
tm.assert_index_equal(bf.columns, other.columns)
tm.assert_index_equal(bf.index, other.index)
tm.assert_index_equal(af.index, other.index)

# axis = 1
other = float_frame.iloc[:-5, :3].copy()
af, bf = float_frame.align(other, axis=1)
tm.assert_index_equal(bf.columns, float_frame.columns)
tm.assert_index_equal(bf.index, other.index)

# test fill value
join_idx = float_frame.index.join(other.index)
diff_a = float_frame.index.difference(join_idx)
diff_a_vals = af.reindex(diff_a).values

assert (diff_a_vals == -1).all()

af, bf = float_frame.align(other, join="inner", axis=1)
tm.assert_index_equal(bf.columns, other.columns)

af, bf = float_frame.align(other, join="inner", axis=1, method="pad")
tm.assert_index_equal(bf.columns, other.columns)

af, bf = float_frame.align(
    other.iloc[:, 0], join="inner", axis=1, method=None, fill_value=None
)
tm.assert_index_equal(bf.index, Index([]))

af, bf = float_frame.align(
    other.iloc[:, 0], join="inner", axis=1, method=None, fill_value=0
)
tm.assert_index_equal(bf.index, Index([]))

# Try to align DataFrame to Series along bad axis
msg = "No axis named 2 for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    float_frame.align(af.iloc[0, :3], join="inner", axis=2)

# align dataframe to series with broadcast or not
idx = float_frame.index
s = Series(range(len(idx)), index=idx)

left, right = float_frame.align(s, axis=0)
tm.assert_index_equal(left.index, float_frame.index)
tm.assert_index_equal(right.index, float_frame.index)
assert isinstance(right, Series)

left, right = float_frame.align(s, broadcast_axis=1)
tm.assert_index_equal(left.index, float_frame.index)
expected = {c: s for c in float_frame.columns}
expected = DataFrame(
    expected, index=float_frame.index, columns=float_frame.columns
)
tm.assert_frame_equal(right, expected)

# see gh-9558
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
result = df[df["a"] == 2]
expected = DataFrame([[2, 5]], index=[1], columns=["a", "b"])
tm.assert_frame_equal(result, expected)

result = df.where(df["a"] == 2, 0)
expected = DataFrame({"a": [0, 2, 0], "b": [0, 5, 0]})
tm.assert_frame_equal(result, expected)
