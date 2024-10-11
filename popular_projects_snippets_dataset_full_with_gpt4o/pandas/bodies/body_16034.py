# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_describe.py
# GH#48340 - describe should always return float on non-complex numeric input
if is_extension_array_dtype(any_numeric_dtype):
    dtype = "Float64"
else:
    dtype = "complex128" if is_complex_dtype(any_numeric_dtype) else None

ser = Series([0, 1], dtype=any_numeric_dtype)
if dtype == "complex128" and is_numpy_dev:
    with pytest.raises(
        TypeError, match=r"^a must be an array of real numbers$"
    ):
        ser.describe()
    exit()
result = ser.describe()
expected = Series(
    [
        2.0,
        0.5,
        ser.std(),
        0,
        0.25,
        0.5,
        0.75,
        1.0,
    ],
    index=["count", "mean", "std", "min", "25%", "50%", "75%", "max"],
    dtype=dtype,
)
tm.assert_series_equal(result, expected)
