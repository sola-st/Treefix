# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#26919 match Series by not casting np.nan to meaningless int
arr = np.array([[1, np.nan], [2, 3]])
msg = r"Cannot convert non-finite values \(NA or inf\) to integer"
with pytest.raises(IntCastingNaNError, match=msg):
    DataFrame(arr, dtype="i8")

# check this matches Series behavior
with pytest.raises(IntCastingNaNError, match=msg):
    Series(arr[0], dtype="i8", name=0)
