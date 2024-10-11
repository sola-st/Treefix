# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/25403
pa = period_array([pd.Period("2019-01-01")])
arr = np.asarray(pa, dtype="object")
arr.setflags(write=False)

result = period_array(arr)
tm.assert_period_array_equal(result, pa)

result = pd.Series(arr)
tm.assert_series_equal(result, pd.Series(pa))

result = pd.DataFrame({"A": arr})
tm.assert_frame_equal(result, pd.DataFrame({"A": pa}))
