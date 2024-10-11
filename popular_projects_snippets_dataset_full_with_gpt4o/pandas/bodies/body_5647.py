# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
exp_first = np.array(
    [False, False, True, False, False, True, False, True, True, False]
)
exp_last = np.array(
    [True, True, True, True, False, False, False, False, False, False]
)
exp_false = exp_first | exp_last

res_first = algos.duplicated(case, keep="first")
tm.assert_numpy_array_equal(res_first, exp_first)

res_last = algos.duplicated(case, keep="last")
tm.assert_numpy_array_equal(res_last, exp_last)

res_false = algos.duplicated(case, keep=False)
tm.assert_numpy_array_equal(res_false, exp_false)

# index
for idx in [Index(case), Index(case, dtype="category")]:
    res_first = idx.duplicated(keep="first")
    tm.assert_numpy_array_equal(res_first, exp_first)

    res_last = idx.duplicated(keep="last")
    tm.assert_numpy_array_equal(res_last, exp_last)

    res_false = idx.duplicated(keep=False)
    tm.assert_numpy_array_equal(res_false, exp_false)

# series
for s in [Series(case), Series(case, dtype="category")]:
    res_first = s.duplicated(keep="first")
    tm.assert_series_equal(res_first, Series(exp_first))

    res_last = s.duplicated(keep="last")
    tm.assert_series_equal(res_last, Series(exp_last))

    res_false = s.duplicated(keep=False)
    tm.assert_series_equal(res_false, Series(exp_false))
