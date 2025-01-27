# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_frame.py
datetime_series.name = None
rs = datetime_series.to_frame()
xp = DataFrame(datetime_series.values, index=datetime_series.index)
tm.assert_frame_equal(rs, xp)

datetime_series.name = "testname"
rs = datetime_series.to_frame()
xp = DataFrame(
    {"testname": datetime_series.values}, index=datetime_series.index
)
tm.assert_frame_equal(rs, xp)

rs = datetime_series.to_frame(name="testdifferent")
xp = DataFrame(
    {"testdifferent": datetime_series.values}, index=datetime_series.index
)
tm.assert_frame_equal(rs, xp)
