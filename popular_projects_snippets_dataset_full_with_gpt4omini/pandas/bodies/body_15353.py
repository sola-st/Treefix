# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
result = datetime_series[datetime_series > 0]
assert result.name == datetime_series.name

result = datetime_series[[0, 2, 4]]
assert result.name == datetime_series.name

result = datetime_series[5:10]
assert result.name == datetime_series.name
