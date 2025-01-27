# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
# GH 13149, GH 13209
idx = DatetimeIndex(["2016-05-16", "NaT", NaT, np.NaN])
msg = "Cannot cast DatetimeIndex to dtype"
if dtype == "datetime64":
    msg = "Casting to unit-less dtype 'datetime64' is not supported"
with pytest.raises(TypeError, match=msg):
    idx.astype(dtype)
