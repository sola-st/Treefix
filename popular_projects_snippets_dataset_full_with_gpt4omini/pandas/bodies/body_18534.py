# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
# issue 20684
msg = "Argument 'date_string' has incorrect type (expected str, got tuple)"
with pytest.raises(TypeError, match=re.escape(msg)):
    parse_datetime_string_with_reso((1, 2, 3))

result = parse_datetime_string_with_reso("2019")
expected = (datetime(2019, 1, 1), "year")
assert result == expected
