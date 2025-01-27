# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 3888 (strings)
expected = to_datetime(["2012"], cache=cache)[0]
result = to_datetime("2012", cache=cache)
assert result == expected
