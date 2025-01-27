# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
ambiguous_string = "01/01/2011"
result = parsing.guess_datetime_format(ambiguous_string, dayfirst=dayfirst)
assert result == expected
