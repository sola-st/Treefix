# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
tz = tz_aware_fixture

dti = date_range("2016-01-01", periods=365, freq="B", tz=tz)
dta = dti._data.as_unit("s")

res = frequencies.infer_freq(dta)
assert res == "B"
