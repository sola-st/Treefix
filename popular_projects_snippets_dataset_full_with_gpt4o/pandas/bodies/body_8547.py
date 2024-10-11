# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH#48659
dti = date_range("2016-01-01", periods=10, tz="UTC")

msg = "Passed data is timezone-aware, incompatible with 'tz=None'"
with pytest.raises(ValueError, match=msg):
    DatetimeIndex(dti, tz=None)

with pytest.raises(ValueError, match=msg):
    DatetimeIndex(np.array(dti), tz=None)

msg = "Cannot pass both a timezone-aware dtype and tz=None"
with pytest.raises(ValueError, match=msg):
    DatetimeIndex([], dtype="M8[ns, UTC]", tz=None)
