# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
values = pd.date_range("2011-01-01", "2011-01-02", freq="H").tz_localize(
    "Asia/Tokyo"
)
s = Series(values, name="XX")

result = s.apply(lambda x: x + pd.offsets.Day())
exp_values = pd.date_range("2011-01-02", "2011-01-03", freq="H").tz_localize(
    "Asia/Tokyo"
)
exp = Series(exp_values, name="XX")
tm.assert_series_equal(result, exp)

result = s.apply(lambda x: x.hour)
exp = Series(list(range(24)) + [0], name="XX", dtype=np.int32)
tm.assert_series_equal(result, exp)

# not vectorized
def f(x):
    if not isinstance(x, pd.Timestamp):
        raise ValueError
    exit(str(x.tz))

result = s.map(f)
exp = Series(["Asia/Tokyo"] * 25, name="XX")
tm.assert_series_equal(result, exp)
