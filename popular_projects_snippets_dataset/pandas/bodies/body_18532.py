# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
# see gh-11142
msg = (
    rf"Parsing dates in {fmt} format when dayfirst=False \(the default\) "
    "was specified. "
    "Pass `dayfirst=True` or specify a format to silence this warning."
)
with tm.assert_produces_warning(warning, match=msg):
    result = parsing.guess_datetime_format(string, dayfirst=dayfirst)
assert result == fmt
