# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# https://github.com/pandas-dev/pandas/issues/50412
# the formats alternate between ISO8601 and non-ISO8601 to check both paths
result = to_datetime(
    "2000-01-03 12:34:56.123456+01:00", format=format, exact=False
)
assert result == expected
