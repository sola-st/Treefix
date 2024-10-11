# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
with pytest.raises(parsing.DateParseError, match=msg):
    parsing.parse_datetime_string_with_reso(date_str, **kwargs)
