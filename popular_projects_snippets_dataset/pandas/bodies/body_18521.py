# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
msg = f"Unknown datetime string format, unable to parse: {dashed}"

with pytest.raises(parsing.DateParseError, match=msg):
    parse_datetime_string_with_reso(dashed)
