# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
result = string_series.map(lambda x: Decimal(str(x)))
assert result.dtype == np.object_
assert isinstance(result[0], Decimal)
