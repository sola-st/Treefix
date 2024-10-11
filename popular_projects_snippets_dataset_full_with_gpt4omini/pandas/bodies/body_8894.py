# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
left, right = left_right_dtypes
left = left.copy(deep=True)
right = right.copy(deep=True)
arr = IntervalArray.from_arrays(left, right)

msg = "`axis` must be fewer than the number of dimensions"
for axis in [-2, 1]:
    with pytest.raises(ValueError, match=msg):
        arr.min(axis=axis)
    with pytest.raises(ValueError, match=msg):
        arr.max(axis=axis)

msg = "'>=' not supported between"
with pytest.raises(TypeError, match=msg):
    arr.min(axis="foo")
with pytest.raises(TypeError, match=msg):
    arr.max(axis="foo")
