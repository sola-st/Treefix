# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
strdates = ["1/1/2012", "3/1/2012", "4/1/2012"]
rng = DatetimeIndex(strdates, tz=prefix + "US/Eastern")
assert (rng.hour == 0).all()

# a more unusual time zone, #1946
dr = date_range(
    "2011-10-02 00:00", freq="h", periods=10, tz=prefix + "America/Atikokan"
)

expected = Index(np.arange(10, dtype=np.int32))
tm.assert_index_equal(dr.hour, expected)
