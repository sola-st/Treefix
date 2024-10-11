# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py

dt = [
    "2011-01-01",
    "2011-01-02",
    "2011-01-01",
    "NaT",
    "2011-01-03",
    "2011-01-02",
    "2011-01-04",
    "2011-01-01",
    "NaT",
    "2011-01-06",
]
td = [
    "1 days",
    "2 days",
    "1 days",
    "NaT",
    "3 days",
    "2 days",
    "4 days",
    "1 days",
    "NaT",
    "6 days",
]

cases = [
    np.array([Timestamp(d) for d in dt]),
    np.array([Timestamp(d, tz="US/Eastern") for d in dt]),
    np.array([Period(d, freq="D") for d in dt]),
    np.array([np.datetime64(d) for d in dt]),
    np.array([Timedelta(d) for d in td]),
]

exp_first = np.array(
    [False, False, True, False, False, True, False, True, True, False]
)
exp_last = np.array(
    [True, True, True, True, False, False, False, False, False, False]
)
exp_false = exp_first | exp_last

for case in cases:
    res_first = algos.duplicated(case, keep="first")
    tm.assert_numpy_array_equal(res_first, exp_first)

    res_last = algos.duplicated(case, keep="last")
    tm.assert_numpy_array_equal(res_last, exp_last)

    res_false = algos.duplicated(case, keep=False)
    tm.assert_numpy_array_equal(res_false, exp_false)

    # index
    for idx in [
        Index(case),
        Index(case, dtype="category"),
        Index(case, dtype=object),
    ]:
        res_first = idx.duplicated(keep="first")
        tm.assert_numpy_array_equal(res_first, exp_first)

        res_last = idx.duplicated(keep="last")
        tm.assert_numpy_array_equal(res_last, exp_last)

        res_false = idx.duplicated(keep=False)
        tm.assert_numpy_array_equal(res_false, exp_false)

    # series
    for s in [
        Series(case),
        Series(case, dtype="category"),
        Series(case, dtype=object),
    ]:
        res_first = s.duplicated(keep="first")
        tm.assert_series_equal(res_first, Series(exp_first))

        res_last = s.duplicated(keep="last")
        tm.assert_series_equal(res_last, Series(exp_last))

        res_false = s.duplicated(keep=False)
        tm.assert_series_equal(res_false, Series(exp_false))
