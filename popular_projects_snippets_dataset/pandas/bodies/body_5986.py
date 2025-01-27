# Extracted from ./data/repos/pandas/pandas/tests/extension/test_integer.py
# overwrite to ensure pd.NA is tested instead of np.nan
# https://github.com/pandas-dev/pandas/issues/30958
length = 64
if not IS64 or is_platform_windows():
    if not s.dtype.itemsize == 8:
        length = 32

if s.dtype.name.startswith("U"):
    expected_dtype = f"UInt{length}"
else:
    expected_dtype = f"Int{length}"

if op_name == "cumsum":
    result = getattr(s, op_name)(skipna=skipna)
    expected = pd.Series(
        pd.array(
            getattr(s.astype("float64"), op_name)(skipna=skipna),
            dtype=expected_dtype,
        )
    )
    tm.assert_series_equal(result, expected)
elif op_name in ["cummax", "cummin"]:
    result = getattr(s, op_name)(skipna=skipna)
    expected = pd.Series(
        pd.array(
            getattr(s.astype("float64"), op_name)(skipna=skipna),
            dtype=s.dtype,
        )
    )
    tm.assert_series_equal(result, expected)
elif op_name == "cumprod":
    result = getattr(s[:12], op_name)(skipna=skipna)
    expected = pd.Series(
        pd.array(
            getattr(s[:12].astype("float64"), op_name)(skipna=skipna),
            dtype=expected_dtype,
        )
    )
    tm.assert_series_equal(result, expected)

else:
    raise NotImplementedError(f"{op_name} not supported")
