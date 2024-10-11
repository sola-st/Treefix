# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 7594
# don't coerce tz-aware
tz = pytz.timezone("US/Eastern")
dt = tz.localize(datetime(2012, 1, 1))

df = DataFrame({"End Date": dt}, index=[0])
assert df.iat[0, 0] == dt
tm.assert_series_equal(
    df.dtypes, Series({"End Date": "datetime64[ns, US/Eastern]"})
)

df = DataFrame([{"End Date": dt}])
assert df.iat[0, 0] == dt
tm.assert_series_equal(
    df.dtypes, Series({"End Date": "datetime64[ns, US/Eastern]"})
)
