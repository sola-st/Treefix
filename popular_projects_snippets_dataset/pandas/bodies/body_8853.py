# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
# GH#50082
dti = pd.date_range("2016-01-01", periods=4)
dta = dti._data
result = dta.astype("Sparse[datetime64[ns]]")

assert result.dtype == "Sparse[datetime64[ns]]"
assert (result == dta).all()
