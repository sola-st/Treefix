# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dti = pd.date_range("2016-01-01", periods=3)

res = dti.astype("M8[s]")
assert res.dtype == "M8[s]"

dta = dti._data
res = dta.astype("M8[s]")
assert res.dtype == "M8[s]"
assert isinstance(res, pd.core.arrays.DatetimeArray)  # used to be ndarray
