# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
dtype = np.dtype(dtype)
vals = np.array([pd.NaT, val], dtype=object)
result = lib.maybe_convert_objects(
    vals,
    convert_datetime=True,
    convert_timedelta=True,
    dtype_if_all_nat=dtype,
)
assert result.dtype == dtype
assert np.isnat(result).all()

result = lib.maybe_convert_objects(
    vals[::-1],
    convert_datetime=True,
    convert_timedelta=True,
    dtype_if_all_nat=dtype,
)
assert result.dtype == dtype
assert np.isnat(result).all()
