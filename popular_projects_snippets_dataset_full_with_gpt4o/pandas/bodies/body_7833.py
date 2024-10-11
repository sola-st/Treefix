# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period.py
idx = PeriodIndex([], freq="M")

exp = np.array([], dtype=np.int64)
tm.assert_numpy_array_equal(idx.view("i8"), exp)
tm.assert_numpy_array_equal(idx.asi8, exp)

idx = PeriodIndex(["2011-01", NaT], freq="M")

exp = np.array([492, -9223372036854775808], dtype=np.int64)
tm.assert_numpy_array_equal(idx.view("i8"), exp)
tm.assert_numpy_array_equal(idx.asi8, exp)

exp = np.array([14975, -9223372036854775808], dtype=np.int64)
idx = PeriodIndex(["2011-01-01", NaT], freq="D")
tm.assert_numpy_array_equal(idx.view("i8"), exp)
tm.assert_numpy_array_equal(idx.asi8, exp)
