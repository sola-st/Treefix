# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_argsort.py
result = datetime_series.argsort()
assert result.name == datetime_series.name
