# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
# https://github.com/pandas-dev/pandas/issues/49043
result = parsing.guess_datetime_format(input)
expected = "%Y-%m-%dT%H:%M:%S.%f"
assert result == expected
