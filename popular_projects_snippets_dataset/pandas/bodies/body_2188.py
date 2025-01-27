# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# ints
result = Timestamp(0)
expected = to_datetime(0, cache=cache)
assert result == expected
