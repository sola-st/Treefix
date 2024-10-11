# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_copy.py
result = datetime_series.copy()
assert result.name == datetime_series.name
