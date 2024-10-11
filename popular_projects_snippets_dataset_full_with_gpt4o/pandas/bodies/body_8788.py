# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
arr = cls._from_sequence(["a", "b"])

if cls is pd.arrays.StringArray:
    msg = "Cannot set non-string value '10' into a StringArray."
else:
    msg = "Scalar must be NA or str"
with pytest.raises(ValueError, match=msg):
    arr[0] = 10

if cls is pd.arrays.StringArray:
    msg = "Must provide strings."
else:
    msg = "Scalar must be NA or str"
with pytest.raises(ValueError, match=msg):
    arr[:] = np.array([1, 2])
