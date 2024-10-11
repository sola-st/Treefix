# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py

r = test_series.resample("H")
result = r.mean()
assert isinstance(result, Series)
assert len(result) == 217

r = test_series.to_frame().resample("H")
result = r.mean()
assert isinstance(result, DataFrame)
assert len(result) == 217
