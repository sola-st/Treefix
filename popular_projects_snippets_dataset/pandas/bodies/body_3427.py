# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_at_time.py
# GH#24043
dti = date_range("2018", periods=3, freq="H", tz="US/Pacific")
df = DataFrame(list(range(len(dti))), index=dti)
result = df.at_time(time(4, tzinfo=pytz.timezone("US/Eastern")))
expected = df.iloc[1:2]
tm.assert_frame_equal(result, expected)
