# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py

# GH 4576
# boolean comparisons with a tuple/list give unexpected results
df = DataFrame(np.arange(6).reshape((3, 2)))
b = np.array([2, 2])
b_r = np.atleast_2d([2, 2])
b_c = b_r.T
lst = [2, 2, 2]
tup = tuple(lst)

# gt
expected = DataFrame([[False, False], [False, True], [True, True]])
result = df > b
tm.assert_frame_equal(result, expected)

result = df.values > b
tm.assert_numpy_array_equal(result, expected.values)

msg1d = "Unable to coerce to Series, length must be 2: given 3"
msg2d = "Unable to coerce to DataFrame, shape must be"
msg2db = "operands could not be broadcast together with shapes"
with pytest.raises(ValueError, match=msg1d):
    # wrong shape
    df > lst

with pytest.raises(ValueError, match=msg1d):
    # wrong shape
    df > tup

# broadcasts like ndarray (GH#23000)
result = df > b_r
tm.assert_frame_equal(result, expected)

result = df.values > b_r
tm.assert_numpy_array_equal(result, expected.values)

with pytest.raises(ValueError, match=msg2d):
    df > b_c

with pytest.raises(ValueError, match=msg2db):
    df.values > b_c

# ==
expected = DataFrame([[False, False], [True, False], [False, False]])
result = df == b
tm.assert_frame_equal(result, expected)

with pytest.raises(ValueError, match=msg1d):
    df == lst

with pytest.raises(ValueError, match=msg1d):
    df == tup

# broadcasts like ndarray (GH#23000)
result = df == b_r
tm.assert_frame_equal(result, expected)

result = df.values == b_r
tm.assert_numpy_array_equal(result, expected.values)

with pytest.raises(ValueError, match=msg2d):
    df == b_c

assert df.values.shape != b_c.shape

# with alignment
df = DataFrame(
    np.arange(6).reshape((3, 2)), columns=list("AB"), index=list("abc")
)
expected.index = df.index
expected.columns = df.columns

with pytest.raises(ValueError, match=msg1d):
    df == lst

with pytest.raises(ValueError, match=msg1d):
    df == tup
