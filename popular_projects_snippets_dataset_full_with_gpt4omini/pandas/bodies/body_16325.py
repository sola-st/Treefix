# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# tests all units
# gh-19223
# TODO: GH#19223 was about .astype, doesn't belong here
dtype = f"{kind}8[{unit}]"
arr = np.array([1, 2, 3], dtype=arr_dtype)
ser = Series(arr)
result = ser.astype(dtype)

expected = Series(arr.astype(dtype))

if unit in ["ns", "us", "ms", "s"]:
    assert result.dtype == dtype
    assert expected.dtype == dtype
else:
    # Otherwise we cast to nearest-supported unit, i.e. seconds
    assert result.dtype == f"{kind}8[s]"
    assert expected.dtype == f"{kind}8[s]"

tm.assert_series_equal(result, expected)
