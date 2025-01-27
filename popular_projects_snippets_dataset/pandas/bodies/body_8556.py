# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
tz = tz_aware_fixture
i = date_range("20130101", periods=5, freq="H", tz=tz)
i = i._with_freq(None)
kwargs = {key: attrgetter(val)(i) for key, val in kwargs.items()}

if "tz" in kwargs:
    result = DatetimeIndex(i.asi8, tz="UTC").tz_convert(kwargs["tz"])

    expected = DatetimeIndex(i, **kwargs)
    tm.assert_index_equal(result, expected)

# localize into the provided tz
i2 = DatetimeIndex(i.tz_localize(None).asi8, tz="UTC")
expected = i.tz_localize(None).tz_localize("UTC")
tm.assert_index_equal(i2, expected)

# incompat tz/dtype
msg = "cannot supply both a tz and a dtype with a tz"
with pytest.raises(ValueError, match=msg):
    DatetimeIndex(i.tz_localize(None).asi8, dtype=i.dtype, tz="US/Pacific")
