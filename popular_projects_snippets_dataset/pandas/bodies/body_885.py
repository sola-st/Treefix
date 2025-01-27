# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
arr = np.array([1, 3, 4, 9], dtype=dtype)
ii = IntervalIndex.from_breaks(arr)
blk = new_block(ii._data, [1], ndim=2)

elem = element(ii)
self.check_series_setitem(elem, ii, True)
assert blk._can_hold_element(elem)

# Careful: to get the expected Series-inplace behavior we need
# `elem` to not have the same length as `arr`
ii2 = IntervalIndex.from_breaks(arr[:-1], closed="neither")
elem = element(ii2)
self.check_series_setitem(elem, ii, False)
assert not blk._can_hold_element(elem)

ii3 = IntervalIndex.from_breaks([Timestamp(1), Timestamp(3), Timestamp(4)])
elem = element(ii3)
self.check_series_setitem(elem, ii, False)
assert not blk._can_hold_element(elem)

ii4 = IntervalIndex.from_breaks([Timedelta(1), Timedelta(3), Timedelta(4)])
elem = element(ii4)
self.check_series_setitem(elem, ii, False)
assert not blk._can_hold_element(elem)
