# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
dta = date_range("2016-01-01", periods=3, tz="US/Pacific")._data

msg = "cannot diff DatetimeArray on axis=1"
with pytest.raises(ValueError, match=msg):
    algos.diff(dta, 1, axis=1)
