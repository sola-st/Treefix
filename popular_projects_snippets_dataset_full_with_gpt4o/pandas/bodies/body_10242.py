# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py

# combining multiple / different timezones yields UTC

data = """0,2000-01-28 16:47:00,America/Chicago
1,2000-01-29 16:48:00,America/Chicago
2,2000-01-30 16:49:00,America/Los_Angeles
3,2000-01-31 16:50:00,America/Chicago
4,2000-01-01 16:50:00,America/New_York"""

df = pd.read_csv(StringIO(data), header=None, names=["value", "date", "tz"])
result = df.groupby("tz", group_keys=False).date.apply(
    lambda x: pd.to_datetime(x).dt.tz_localize(x.name)
)

expected = Series(
    [
        Timestamp("2000-01-28 16:47:00-0600", tz="America/Chicago"),
        Timestamp("2000-01-29 16:48:00-0600", tz="America/Chicago"),
        Timestamp("2000-01-30 16:49:00-0800", tz="America/Los_Angeles"),
        Timestamp("2000-01-31 16:50:00-0600", tz="America/Chicago"),
        Timestamp("2000-01-01 16:50:00-0500", tz="America/New_York"),
    ],
    name="date",
    dtype=object,
)
tm.assert_series_equal(result, expected)

tz = "America/Chicago"
res_values = df.groupby("tz").date.get_group(tz)
result = pd.to_datetime(res_values).dt.tz_localize(tz)
exp_values = Series(
    ["2000-01-28 16:47:00", "2000-01-29 16:48:00", "2000-01-31 16:50:00"],
    index=[0, 1, 3],
    name="date",
)
expected = pd.to_datetime(exp_values).dt.tz_localize(tz)
tm.assert_series_equal(result, expected)
