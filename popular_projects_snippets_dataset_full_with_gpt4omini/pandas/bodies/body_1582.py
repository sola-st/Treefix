# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# indexing - setting an element
df = DataFrame(
    data=to_datetime(["2015-03-30 20:12:32", "2015-03-12 00:11:11"]),
    columns=["time"],
)
df["new_col"] = ["new", "old"]
df.time = df.set_index("time").index.tz_localize("UTC")
v = df[df.new_col == "new"].set_index("time").index.tz_convert("US/Pacific")

# pre-2.0  trying to set a single element on a part of a different
#  timezone converted to object; in 2.0 it retains dtype
df2 = df.copy()
df2.loc[df2.new_col == "new", "time"] = v

expected = Series([v[0].tz_convert("UTC"), df.loc[1, "time"]], name="time")
tm.assert_series_equal(df2.time, expected)

v = df.loc[df.new_col == "new", "time"] + Timedelta("1s")
df.loc[df.new_col == "new", "time"] = v
tm.assert_series_equal(df.loc[df.new_col == "new", "time"], v)
