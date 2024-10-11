# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_array_to_datetime.py
arr = np.array(data, dtype=object)
result, _ = tslib.array_to_datetime(arr)

expected = np.array(expected, dtype="M8[ns]")
tm.assert_numpy_array_equal(result, expected)
