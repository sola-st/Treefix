# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
# GH #771
a = bdate_range("11/30/2011", "12/31/2011", freq="C")
b = bdate_range("12/10/2011", "12/20/2011", freq="C")
result = a.intersection(b)
tm.assert_index_equal(result, b)
assert result.freq == b.freq
