# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_dropna.py
datetime_series[:5] = np.nan
result = datetime_series.dropna()
assert result.name == datetime_series.name
name = datetime_series.name
ts = datetime_series.copy()
return_value = ts.dropna(inplace=True)
assert return_value is None
assert ts.name == name
