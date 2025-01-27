# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
datetime_series = tm.makeTimeSeries(nper=30)
datetime_series_short = tm.makeTimeSeries(nper=25)

# GH19018
# initialization ordering: by insertion order if python>= 3.6
d = {"b": datetime_series_short, "a": datetime_series}
frame = DataFrame(data=d)
expected = DataFrame(data=d, columns=list("ba"))
tm.assert_frame_equal(frame, expected)
