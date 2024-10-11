# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
dr = date_range("2011-12-01", "2012-07-20", freq="D", tz=tz)

obj = frame_or_series(np.random.randn(len(dr)), index=dr)

# it works!
obj.asfreq("T")
