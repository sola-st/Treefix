# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# GH 8371
# odd results when rounding is needed

data = """date,time,value
11-08-2014,00:00:01.093,1
11-08-2014,00:00:02.159,1
11-08-2014,00:00:02.667,1
11-08-2014,00:00:03.175,1
11-08-2014,00:00:07.058,1
11-08-2014,00:00:07.362,1
11-08-2014,00:00:08.324,1
11-08-2014,00:00:08.830,1
11-08-2014,00:00:08.982,1
11-08-2014,00:00:09.815,1
11-08-2014,00:00:10.540,1
11-08-2014,00:00:11.061,1
11-08-2014,00:00:11.617,1
11-08-2014,00:00:13.607,1
11-08-2014,00:00:14.535,1
11-08-2014,00:00:15.525,1
11-08-2014,00:00:17.960,1
11-08-2014,00:00:20.674,1
11-08-2014,00:00:21.191,1"""

df = pd.read_csv(
    StringIO(data),
    parse_dates={"timestamp": ["date", "time"]},
    index_col="timestamp",
)
df.index = df.index.as_unit(unit)
df.index.name = None
result = df.resample("6s").sum()
expected = DataFrame(
    {"value": [4, 9, 4, 2]},
    index=date_range("2014-11-08", freq="6s", periods=4).as_unit(unit),
)
tm.assert_frame_equal(result, expected)

result = df.resample("7s").sum()
expected = DataFrame(
    {"value": [4, 10, 4, 1]},
    index=date_range("2014-11-08", freq="7s", periods=4).as_unit(unit),
)
tm.assert_frame_equal(result, expected)

result = df.resample("11s").sum()
expected = DataFrame(
    {"value": [11, 8]},
    index=date_range("2014-11-08", freq="11s", periods=2).as_unit(unit),
)
tm.assert_frame_equal(result, expected)

result = df.resample("13s").sum()
expected = DataFrame(
    {"value": [13, 6]},
    index=date_range("2014-11-08", freq="13s", periods=2).as_unit(unit),
)
tm.assert_frame_equal(result, expected)

result = df.resample("17s").sum()
expected = DataFrame(
    {"value": [16, 3]},
    index=date_range("2014-11-08", freq="17s", periods=2).as_unit(unit),
)
tm.assert_frame_equal(result, expected)
