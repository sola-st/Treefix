# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# GH35227
result = nanops.check_below_min_count((21, 37), None, min_count)
expected_result = False
assert result == expected_result
