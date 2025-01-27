# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
with tm.maybe_produces_warning(
    UserWarning, fmt is not None and re.search(r"%d.*%m", fmt)
):
    result = parsing.guess_datetime_format(string)
assert result == fmt
