# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
"""Helper to get expected range from a both inclusive range"""
left_match = begin_to_match == both_range[0]
right_match = end_to_match == both_range[-1]

if inclusive_endpoints == "left" and right_match:
    expected_range = both_range[:-1]
elif inclusive_endpoints == "right" and left_match:
    expected_range = both_range[1:]
elif inclusive_endpoints == "neither" and left_match and right_match:
    expected_range = both_range[1:-1]
elif inclusive_endpoints == "neither" and right_match:
    expected_range = both_range[:-1]
elif inclusive_endpoints == "neither" and left_match:
    expected_range = both_range[1:]
elif inclusive_endpoints == "both":
    expected_range = both_range[:]
else:
    expected_range = both_range[:]

exit(expected_range)
