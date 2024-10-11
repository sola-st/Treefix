# Extracted from ./data/repos/pandas/pandas/tests/base/test_constructors.py
arr = np.array(["2020-01-01T00:00:00.000000"], dtype="datetime64[us]")
dta = pd.core.arrays.DatetimeArray._simple_new(arr, dtype=arr.dtype)
expected = constructor(dta)
assert expected.dtype == arr.dtype

result = constructor(arr)
tm.assert_equal(result, expected)

# https://github.com/pandas-dev/pandas/issues/34843
arr.flags.writeable = False
result = constructor(arr)
tm.assert_equal(result, expected)
