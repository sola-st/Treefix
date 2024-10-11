# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#30976
ms = np.datetime64(1, "ms")
arr = np.array([np.datetime64(1, "ms")], dtype=">M8[ms]")

result = Series(arr)
expected = Series([Timestamp(ms)]).astype("M8[ms]")
assert expected.dtype == "M8[ms]"
tm.assert_series_equal(result, expected)
