# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period.py
idx = PeriodIndex([], freq="M")

exp = np.array([], dtype=object)
tm.assert_numpy_array_equal(idx.values, exp)
tm.assert_numpy_array_equal(idx.to_numpy(), exp)

exp = np.array([], dtype=np.int64)
tm.assert_numpy_array_equal(idx.asi8, exp)

idx = PeriodIndex(["2011-01", NaT], freq="M")

exp = np.array([Period("2011-01", freq="M"), NaT], dtype=object)
tm.assert_numpy_array_equal(idx.values, exp)
tm.assert_numpy_array_equal(idx.to_numpy(), exp)
exp = np.array([492, -9223372036854775808], dtype=np.int64)
tm.assert_numpy_array_equal(idx.asi8, exp)

idx = PeriodIndex(["2011-01-01", NaT], freq="D")

exp = np.array([Period("2011-01-01", freq="D"), NaT], dtype=object)
tm.assert_numpy_array_equal(idx.values, exp)
tm.assert_numpy_array_equal(idx.to_numpy(), exp)
exp = np.array([14975, -9223372036854775808], dtype=np.int64)
tm.assert_numpy_array_equal(idx.asi8, exp)
