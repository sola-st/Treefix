# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# https://github.com/pandas-dev/pandas/issues/12649
expected = Timestamp(2020, 1, 1)
result = to_datetime(input, format=format)
assert result == expected
