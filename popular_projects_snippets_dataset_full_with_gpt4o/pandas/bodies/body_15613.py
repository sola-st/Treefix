# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_combine_first.py
result = datetime_series.combine_first(datetime_series[:5])
assert result.name == datetime_series.name
