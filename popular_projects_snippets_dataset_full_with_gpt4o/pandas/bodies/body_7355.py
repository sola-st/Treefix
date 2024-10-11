# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
# GH#23539
# passing tz-aware DatetimeIndex raises, naive or ndarray[datetime64]
#  raise as of GH#29794
dti = pd.date_range("2016-01-01", periods=3)

msg = "cannot be converted to timedelta64"
with pytest.raises(TypeError, match=msg):
    TimedeltaIndex(dti.tz_localize("Europe/Brussels"))

with pytest.raises(TypeError, match=msg):
    TimedeltaIndex(dti)

with pytest.raises(TypeError, match=msg):
    TimedeltaIndex(np.asarray(dti))
