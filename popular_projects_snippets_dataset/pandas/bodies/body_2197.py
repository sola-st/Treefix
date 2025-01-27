# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH #999, #858

strings = np.array(["1/1/2000", "1/2/2000", np.nan, "1/4/2000"], dtype=object)

expected = np.empty(4, dtype="M8[ns]")
for i, val in enumerate(strings):
    if isna(val):
        expected[i] = iNaT
    else:
        expected[i] = parse(val)

result = tslib.array_to_datetime(strings)[0]
tm.assert_almost_equal(result, expected)

result2 = to_datetime(strings, cache=cache)
assert isinstance(result2, DatetimeIndex)
tm.assert_numpy_array_equal(result, result2.values)
