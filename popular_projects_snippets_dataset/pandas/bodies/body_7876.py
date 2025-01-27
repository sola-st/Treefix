# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_astype.py
idx = PeriodIndex([], freq="M")

exp = np.array([], dtype=object)
tm.assert_numpy_array_equal(idx.astype(object).values, exp)
tm.assert_numpy_array_equal(idx._mpl_repr(), exp)

idx = PeriodIndex(["2011-01", NaT], freq="M")

exp = np.array([Period("2011-01", freq="M"), NaT], dtype=object)
tm.assert_numpy_array_equal(idx.astype(object).values, exp)
tm.assert_numpy_array_equal(idx._mpl_repr(), exp)

exp = np.array([Period("2011-01-01", freq="D"), NaT], dtype=object)
idx = PeriodIndex(["2011-01-01", NaT], freq="D")
tm.assert_numpy_array_equal(idx.astype(object).values, exp)
tm.assert_numpy_array_equal(idx._mpl_repr(), exp)
