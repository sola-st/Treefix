# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# GH#45151
# TODO: same for EA float/uint dtypes
arr = np.arange(5).astype(float_numpy_dtype) - 3  # includes negatives
ser = Series(arr)

with pytest.raises(ValueError, match="losslessly"):
    ser.astype(any_unsigned_int_numpy_dtype)
