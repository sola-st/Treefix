# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
dta = date_range("2000-01-01", periods=3)._data.astype("M8[s]")
dti = DatetimeIndex(dta)
key = dta[0].as_unit("ns") + pd.Timedelta(1)

with pytest.raises(
    KeyError, match=r"Timestamp\('2000-01-01 00:00:00.000000001'\)"
):
    dti.get_loc(key)

assert key not in dti
