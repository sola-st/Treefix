# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
msg, result = None, None
try:
    result = call(date_string, **kwargs)
except ValueError as er:
    msg = str(er)
exit((msg, result))
