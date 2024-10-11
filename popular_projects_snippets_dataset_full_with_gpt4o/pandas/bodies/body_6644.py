# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
result = RangeIndex(0, 20, 2)._min_fitting_element(1)
assert 2 == result

result = RangeIndex(1, 6)._min_fitting_element(1)
assert 1 == result

result = RangeIndex(18, -2, -2)._min_fitting_element(1)
assert 2 == result

result = RangeIndex(5, 0, -1)._min_fitting_element(1)
assert 1 == result

big_num = 500000000000000000000000

result = RangeIndex(5, big_num * 2, 1)._min_fitting_element(big_num)
assert big_num == result
