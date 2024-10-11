# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parse_iso8601.py
# GH#25895 make sure isoparser doesn't overflow with long input
date_str, expected = ("2013-1-1 5:30:00", datetime(2013, 1, 1, 5, 30))
actual = tslib._test_parse_iso8601(" " * 200 + date_str)
assert actual == expected
