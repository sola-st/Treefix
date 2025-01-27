# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_setops.py
# GH14323: difference of Period MUST preserve frequency
# but the ability to union results must be preserved

index = period_range("20160920", "20160925", freq="D")

other = period_range("20160921", "20160924", freq="D")
expected = PeriodIndex(["20160920", "20160925"], freq="D")
idx_diff = index.difference(other, sort)
tm.assert_index_equal(idx_diff, expected)
tm.assert_attr_equal("freq", idx_diff, expected)

other = period_range("20160922", "20160925", freq="D")
idx_diff = index.difference(other, sort)
expected = PeriodIndex(["20160920", "20160921"], freq="D")
tm.assert_index_equal(idx_diff, expected)
tm.assert_attr_equal("freq", idx_diff, expected)
