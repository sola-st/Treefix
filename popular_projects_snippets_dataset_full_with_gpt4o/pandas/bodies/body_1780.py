# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py

ts = simple_date_range_series("1/1/2000", "4/1/2000")
ts.index = ts.index.as_unit(unit)

result = ts.resample("M").apply(lambda x: x.mean())
exp = ts.resample("M").mean()
tm.assert_series_equal(result, exp)

foo_exp = ts.resample("M").mean()
foo_exp.name = "foo"
bar_exp = ts.resample("M").std()
bar_exp.name = "bar"

result = ts.resample("M").apply([lambda x: x.mean(), lambda x: x.std(ddof=1)])
result.columns = ["foo", "bar"]
tm.assert_series_equal(result["foo"], foo_exp)
tm.assert_series_equal(result["bar"], bar_exp)

# this is a MI Series, so comparing the names of the results
# doesn't make sense
result = ts.resample("M").aggregate(
    {"foo": lambda x: x.mean(), "bar": lambda x: x.std(ddof=1)}
)
tm.assert_series_equal(result["foo"], foo_exp, check_names=False)
tm.assert_series_equal(result["bar"], bar_exp, check_names=False)
