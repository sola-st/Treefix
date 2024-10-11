# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
# GH 18951: tz-naive to tz-aware
idx = date_range("20170101", periods=4)
idx = idx._with_freq(None)  # tz_localize does not preserve freq
msg = "Cannot use .astype to convert from timezone-naive"
with pytest.raises(TypeError, match=msg):
    # dt64->dt64tz deprecated
    idx.astype("datetime64[ns, US/Eastern]")
with pytest.raises(TypeError, match=msg):
    # dt64->dt64tz deprecated
    idx._data.astype("datetime64[ns, US/Eastern]")
