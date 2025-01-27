# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
# GH14323: difference of DatetimeIndex should not preserve frequency

index = date_range("20160920", "20160925", freq="D")
other = date_range("20160921", "20160924", freq="D")
expected = DatetimeIndex(["20160920", "20160925"], freq=None)
idx_diff = index.difference(other, sort)
tm.assert_index_equal(idx_diff, expected)
tm.assert_attr_equal("freq", idx_diff, expected)

other = date_range("20160922", "20160925", freq="D")
idx_diff = index.difference(other, sort)
expected = DatetimeIndex(["20160920", "20160921"], freq=None)
tm.assert_index_equal(idx_diff, expected)
tm.assert_attr_equal("freq", idx_diff, expected)
