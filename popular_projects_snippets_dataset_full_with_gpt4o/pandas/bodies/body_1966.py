# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_time.py
# GH#11818
assert to_time(time_string) == time(14, 15)
