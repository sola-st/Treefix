# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#42505
dt = Timestamp("2019-11-03 01:00:00-0700").tz_convert("America/Los_Angeles")

df = DataFrame({"dt": dt}, index=[0])
expected = DataFrame({"dt": [dt]})
tm.assert_frame_equal(df, expected)

# Non-homogeneous
df = DataFrame({"dt": dt, "value": [1]})
expected = DataFrame({"dt": [dt], "value": [1]})
tm.assert_frame_equal(df, expected)
