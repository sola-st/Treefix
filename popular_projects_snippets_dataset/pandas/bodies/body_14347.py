# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

# 8591
# doc example from tseries holiday section
weekmask_egypt = "Sun Mon Tue Wed Thu"
holidays = [
    "2012-05-01",
    dt.datetime(2013, 5, 1),
    np.datetime64("2014-05-01"),
]
bday_egypt = pd.offsets.CustomBusinessDay(
    holidays=holidays, weekmask=weekmask_egypt
)
mydt = dt.datetime(2013, 4, 30)
dts = date_range(mydt, periods=5, freq=bday_egypt)

s = Series(dts.weekday, dts).map(Series("Mon Tue Wed Thu Fri Sat Sun".split()))

with ensure_clean_store(setup_path) as store:

    store.put("fixed", s)
    result = store.select("fixed")
    tm.assert_series_equal(result, s)

    store.append("table", s)
    result = store.select("table")
    tm.assert_series_equal(result, s)
