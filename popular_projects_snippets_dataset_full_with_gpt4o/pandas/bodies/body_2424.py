# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
index = Index([1.5, 2, 3, 4, 5])
df = DataFrame(np.random.randn(5, 5), index=index)

result = df.loc[1.5:4]
expected = df.reindex([1.5, 2, 3, 4])
tm.assert_frame_equal(result, expected)
assert len(result) == 4

result = df.loc[4:5]
expected = df.reindex([4, 5])  # reindex with int
tm.assert_frame_equal(result, expected, check_index_type=False)
assert len(result) == 2

result = df.loc[4:5]
expected = df.reindex([4.0, 5.0])  # reindex with float
tm.assert_frame_equal(result, expected)
assert len(result) == 2

# loc_float changes this to work properly
result = df.loc[1:2]
expected = df.iloc[0:2]
tm.assert_frame_equal(result, expected)

df.loc[1:2] = 0
result = df[1:2]
assert (result == 0).all().all()

# #2727
index = Index([1.0, 2.5, 3.5, 4.5, 5.0])
df = DataFrame(np.random.randn(5, 5), index=index)

# positional slicing only via iloc!
msg = (
    "cannot do positional indexing on NumericIndex with "
    r"these indexers \[1.0\] of type float"
)
with pytest.raises(TypeError, match=msg):
    df.iloc[1.0:5]

result = df.iloc[4:5]
expected = df.reindex([5.0])
tm.assert_frame_equal(result, expected)
assert len(result) == 1

cp = df.copy()

with pytest.raises(TypeError, match=_slice_msg):
    cp.iloc[1.0:5] = 0

with pytest.raises(TypeError, match=msg):
    result = cp.iloc[1.0:5] == 0

assert result.values.all()
assert (cp.iloc[0:1] == df.iloc[0:1]).values.all()

cp = df.copy()
cp.iloc[4:5] = 0
assert (cp.iloc[4:5] == 0).values.all()
assert (cp.iloc[0:4] == df.iloc[0:4]).values.all()

# float slicing
result = df.loc[1.0:5]
expected = df
tm.assert_frame_equal(result, expected)
assert len(result) == 5

result = df.loc[1.1:5]
expected = df.reindex([2.5, 3.5, 4.5, 5.0])
tm.assert_frame_equal(result, expected)
assert len(result) == 4

result = df.loc[4.51:5]
expected = df.reindex([5.0])
tm.assert_frame_equal(result, expected)
assert len(result) == 1

result = df.loc[1.0:5.0]
expected = df.reindex([1.0, 2.5, 3.5, 4.5, 5.0])
tm.assert_frame_equal(result, expected)
assert len(result) == 5

cp = df.copy()
cp.loc[1.0:5.0] = 0
result = cp.loc[1.0:5.0]
assert (result == 0).values.all()
