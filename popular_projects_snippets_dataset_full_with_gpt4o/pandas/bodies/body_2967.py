# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# GH#32441
dti = pd.DatetimeIndex(["NaT", "2019-01-01", "2019-01-02"], tz=tz)
ser = Series(dti)

df = ser.to_frame()

result = df.diff()
ex_index = pd.TimedeltaIndex([pd.NaT, pd.NaT, pd.Timedelta(days=1)])
expected = Series(ex_index).to_frame()
tm.assert_frame_equal(result, expected)
