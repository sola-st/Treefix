# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 9431
expected = np.array(
    [
        "2015-01-03T00:00:00.000000000",
        "2015-01-01T00:00:00.000000000",
    ],
    dtype="M8[ns]",
)

dt_index = to_datetime(
    [
        "2015-01-03T00:00:00.000000000",
        "2015-01-01T00:00:00.000000000",
        "2015-01-01T00:00:00.000000000",
    ]
)
result = algos.unique(dt_index)
tm.assert_numpy_array_equal(result, expected)
assert result.dtype == expected.dtype

s = Series(dt_index)
result = algos.unique(s)
tm.assert_numpy_array_equal(result, expected)
assert result.dtype == expected.dtype

arr = s.values
result = algos.unique(arr)
tm.assert_numpy_array_equal(result, expected)
assert result.dtype == expected.dtype
