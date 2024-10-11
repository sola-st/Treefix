# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# mat: 2d matrix with shape (3, 2) to input. empty - makes sized
# objects
mat = empty((2, 3), dtype=float)
# 2-D input
frame = DataFrame(mat, columns=["A", "B", "C"], index=[1, 2])

assert len(frame.index) == 2
assert len(frame.columns) == 3

# 1-D input
frame = DataFrame(empty((3,)), columns=["A"], index=[1, 2, 3])
assert len(frame.index) == 3
assert len(frame.columns) == 1

if empty is not np.ones:
    msg = r"Cannot convert non-finite values \(NA or inf\) to integer"
    with pytest.raises(IntCastingNaNError, match=msg):
        DataFrame(mat, columns=["A", "B", "C"], index=[1, 2], dtype=np.int64)
    exit()
else:
    frame = DataFrame(
        mat, columns=["A", "B", "C"], index=[1, 2], dtype=np.int64
    )
    assert frame.values.dtype == np.int64

# wrong size axis labels
msg = r"Shape of passed values is \(2, 3\), indices imply \(1, 3\)"
with pytest.raises(ValueError, match=msg):
    DataFrame(mat, columns=["A", "B", "C"], index=[1])
msg = r"Shape of passed values is \(2, 3\), indices imply \(2, 2\)"
with pytest.raises(ValueError, match=msg):
    DataFrame(mat, columns=["A", "B"], index=[1, 2])

# higher dim raise exception
with pytest.raises(ValueError, match="Must pass 2-d input"):
    DataFrame(empty((3, 3, 3)), columns=["A", "B", "C"], index=[1])

# automatic labeling
frame = DataFrame(mat)
tm.assert_index_equal(frame.index, Index(range(2)), exact=True)
tm.assert_index_equal(frame.columns, Index(range(3)), exact=True)

frame = DataFrame(mat, index=[1, 2])
tm.assert_index_equal(frame.columns, Index(range(3)), exact=True)

frame = DataFrame(mat, columns=["A", "B", "C"])
tm.assert_index_equal(frame.index, Index(range(2)), exact=True)

# 0-length axis
frame = DataFrame(empty((0, 3)))
assert len(frame.index) == 0

frame = DataFrame(empty((3, 0)))
assert len(frame.columns) == 0
