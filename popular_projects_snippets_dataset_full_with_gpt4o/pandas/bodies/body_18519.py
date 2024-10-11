# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
# Raise on invalid input, don't just return it
msg = "Argument 'date_string' has incorrect type (expected str, got tuple)"
with pytest.raises(TypeError, match=re.escape(msg)):
    parse_datetime_string_with_reso((4, 5))
