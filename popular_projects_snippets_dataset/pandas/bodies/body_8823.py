# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
# https://github.com/pandas-dev/pandas/issues/47628
# setting None with a boolean mask (through _putmaks) should still result
# in pd.NA values in the underlying array
ser = pd.Series(["a", "b", "c"], dtype=dtype)
mask = np.array([False, True, False])

ser[mask] = None
assert ser.array[1] is pd.NA

# for other non-string we should also raise an error
ser = pd.Series(["a", "b", "c"], dtype=dtype)
if type(ser.array) is pd.arrays.StringArray:
    msg = "Cannot set non-string value"
else:
    msg = "Scalar must be NA or str"
with pytest.raises(ValueError, match=msg):
    ser[mask] = 1
