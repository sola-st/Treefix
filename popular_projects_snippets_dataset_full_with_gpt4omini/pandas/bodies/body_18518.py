# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
# GH#46811
parsed, reso = parse_datetime_string_with_reso("2022-04-20 09:19:19.123456789")
assert reso == "nanosecond"
