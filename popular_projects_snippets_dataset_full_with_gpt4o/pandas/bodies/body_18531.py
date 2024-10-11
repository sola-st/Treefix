# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parsing.py
# A datetime string must include a year, month and a day for it to be
# guessable, in addition to being a string that looks like a datetime.
with pytest.raises(
    TypeError,
    match=r"^Argument 'dt_str' has incorrect type \(expected str, got .*\)$",
):
    parsing.guess_datetime_format(invalid_type_dt)
