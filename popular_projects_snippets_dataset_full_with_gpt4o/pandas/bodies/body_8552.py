# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH#23675 deprecated, enforrced in GH#29794
data = np.array([0], dtype="m8[ns]")
msg = r"timedelta64\[ns\] cannot be converted to datetime64"
with pytest.raises(TypeError, match=msg):
    DatetimeIndex(data)

with pytest.raises(TypeError, match=msg):
    to_datetime(data)

with pytest.raises(TypeError, match=msg):
    DatetimeIndex(pd.TimedeltaIndex(data))

with pytest.raises(TypeError, match=msg):
    to_datetime(pd.TimedeltaIndex(data))
