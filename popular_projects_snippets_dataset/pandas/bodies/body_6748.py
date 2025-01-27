# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
# datetime -> timedelta raises
dtype = IntervalDtype("timedelta64[ns]", "right")
msg = "Cannot convert .* to .*; subtypes are incompatible"

index = interval_range(Timestamp("2018-01-01"), periods=10)
with pytest.raises(TypeError, match=msg):
    index.astype(dtype)

index = interval_range(Timestamp("2018-01-01", tz="CET"), periods=10)
with pytest.raises(TypeError, match=msg):
    index.astype(dtype)

# timedelta -> datetime raises
dtype = IntervalDtype("datetime64[ns]", "right")
index = interval_range(Timedelta("0 days"), periods=10)
with pytest.raises(TypeError, match=msg):
    index.astype(dtype)
