# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_hour.py
# gh-49835
idx4 = date_range(start="2014-07-01 10:00", freq="BH", periods=1)
expected4 = DatetimeIndex(["2014-07-01 10:00"], freq="BH")
tm.assert_index_equal(idx4, expected4)
