# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# GH35227
shape = (10, 10)
result = nanops.check_below_min_count(shape, mask, min_count)
assert result == expected_result
