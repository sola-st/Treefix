# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
result, _ = parsing.parse_datetime_string_with_reso(date_str, freq="M")
assert result == expected
