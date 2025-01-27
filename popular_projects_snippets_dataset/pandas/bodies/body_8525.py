# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# GH#14354
empty_idx = date_range(freq="1H", periods=0, end="2015")

right = empty_idx._maybe_cast_slice_bound("2015-01-02", "right")
exp = Timestamp("2015-01-02 23:59:59.999999999")
assert right == exp

left = empty_idx._maybe_cast_slice_bound("2015-01-02", "left")
exp = Timestamp("2015-01-02 00:00:00")
assert left == exp
