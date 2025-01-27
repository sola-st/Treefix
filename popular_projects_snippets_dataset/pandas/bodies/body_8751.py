# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# GH 29578
arr = PeriodArray(PeriodIndex(["2019-01-01", NaT], dtype="period[D]"))

result = arr.strftime("%Y-%m-%d")
expected = np.array(["2019-01-01", np.nan], dtype=object)
tm.assert_numpy_array_equal(result, expected)
