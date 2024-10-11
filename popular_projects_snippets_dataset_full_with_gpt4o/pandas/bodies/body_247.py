# Extracted from ./data/repos/pandas/pandas/tests/apply/test_str.py
result = datetime_series.apply(arg)
expected = getattr(datetime_series, arg)()
assert result == expected
