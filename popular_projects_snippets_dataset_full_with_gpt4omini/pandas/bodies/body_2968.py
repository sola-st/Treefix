# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# diff on NaT values should give NaT, not timedelta64(0)
dti = date_range("2016-01-01", periods=4, tz=tz)
ser = Series(dti)
df = ser.to_frame()

df[1] = ser.copy()

df.iloc[:, 0] = pd.NaT

expected = df - df
assert expected[0].isna().all()

result = df.diff(0, axis=0)
tm.assert_frame_equal(result, expected)

result = df.diff(0, axis=1)
tm.assert_frame_equal(result, expected)
