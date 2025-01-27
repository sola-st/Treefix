# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
result = datetime_series * 2
assert result.name == datetime_series.name
