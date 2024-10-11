# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# just want it to work
start = datetime(2011, 3, 12, tzinfo=pytz.utc)
dr = bdate_range(start, periods=50, freq=pd.offsets.Hour())
assert dr.tz is pytz.utc

# DateRange with naive datetimes
dr = bdate_range("1/1/2005", "1/1/2009", tz=pytz.utc)
dr = bdate_range("1/1/2005", "1/1/2009", tz=tz)

# normalized
central = dr.tz_convert(tz)
assert central.tz is tz
naive = central[0].to_pydatetime().replace(tzinfo=None)
comp = conversion.localize_pydatetime(naive, tz).tzinfo
assert central[0].tz is comp

# compare vs a localized tz
naive = dr[0].to_pydatetime().replace(tzinfo=None)
comp = conversion.localize_pydatetime(naive, tz).tzinfo
assert central[0].tz is comp

# datetimes with tzinfo set
dr = bdate_range(
    datetime(2005, 1, 1, tzinfo=pytz.utc), datetime(2009, 1, 1, tzinfo=pytz.utc)
)
msg = "Start and end cannot both be tz-aware with different timezones"
with pytest.raises(Exception, match=msg):
    bdate_range(datetime(2005, 1, 1, tzinfo=pytz.utc), "1/1/2009", tz=tz)
