# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
tz = tz_aware_fixture
halflife = "23 days"
times = DatetimeIndex(
    ["2020-01-01", "2020-01-10T00:04:05", "2020-02-23T05:00:23"]
).tz_localize(tz)
data = np.arange(3)
df = DataFrame(data)
result = df.ewm(halflife=halflife, times=times).mean()
expected = DataFrame([0.0, 0.5674161888241773, 1.545239952073459])
tm.assert_frame_equal(result, expected)
