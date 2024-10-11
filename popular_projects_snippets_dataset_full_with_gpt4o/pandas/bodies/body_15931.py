# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
result = datetime_series.sort_index(ascending=False)
assert result.name == datetime_series.name
