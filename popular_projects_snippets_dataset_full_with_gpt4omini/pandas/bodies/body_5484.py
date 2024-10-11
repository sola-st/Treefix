# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# https://github.com/pandas-dev/pandas/issues/50231
with tm.assert_produces_warning(None):
    result = Timestamp("13-01-2000")
expected = Timestamp(2000, 1, 13)
assert result == expected
