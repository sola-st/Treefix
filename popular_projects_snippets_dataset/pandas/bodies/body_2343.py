# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_take.py
# homogeneous
order = [3, 1, 2, 0]
for df in [float_frame]:

    result = df.take(order, axis=0)
    expected = df.reindex(df.index.take(order))
    tm.assert_frame_equal(result, expected)

    # axis = 1
    result = df.take(order, axis=1)
    expected = df.loc[:, ["D", "B", "C", "A"]]
    tm.assert_frame_equal(result, expected, check_names=False)

# negative indices
order = [2, 1, -1]
for df in [float_frame]:

    result = df.take(order, axis=0)
    expected = df.reindex(df.index.take(order))
    tm.assert_frame_equal(result, expected)

    result = df.take(order, axis=0)
    tm.assert_frame_equal(result, expected)

    # axis = 1
    result = df.take(order, axis=1)
    expected = df.loc[:, ["C", "B", "D"]]
    tm.assert_frame_equal(result, expected, check_names=False)

# illegal indices
msg = "indices are out-of-bounds"
with pytest.raises(IndexError, match=msg):
    df.take([3, 1, 2, 30], axis=0)
with pytest.raises(IndexError, match=msg):
    df.take([3, 1, 2, -31], axis=0)
with pytest.raises(IndexError, match=msg):
    df.take([3, 1, 2, 5], axis=1)
with pytest.raises(IndexError, match=msg):
    df.take([3, 1, 2, -5], axis=1)
