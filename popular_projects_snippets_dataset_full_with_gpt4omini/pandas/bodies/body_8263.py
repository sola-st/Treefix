# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py

# with tz
rng = date_range("1/1/2000", periods=10, tz="US/Eastern")
msg = "Cannot use .astype to convert from timezone-aware"
with pytest.raises(TypeError, match=msg):
    # deprecated
    rng.astype("datetime64[ns]")
with pytest.raises(TypeError, match=msg):
    # check DatetimeArray while we're here deprecated
    rng._data.astype("datetime64[ns]")
