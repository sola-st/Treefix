# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_constructors.py
# TODO: why TypeError for 'category' but ValueError for i8?
with pytest.raises(
    ValueError, match=r"category cannot be converted to timedelta64\[ns\]"
):
    TimedeltaArray(np.array([1, 2, 3], dtype="i8"), dtype="category")

with pytest.raises(
    ValueError, match=r"dtype int64 cannot be converted to timedelta64\[ns\]"
):
    TimedeltaArray(np.array([1, 2, 3], dtype="i8"), dtype=np.dtype("int64"))
