# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 40951
halflife = "23 days"
times = times_frame.pop("C")
gb = times_frame.groupby("A")
result = gb.ewm(halflife=halflife, times=times).mean()
expected = gb.ewm(halflife=halflife, times=times.values).mean()
tm.assert_frame_equal(result, expected)
