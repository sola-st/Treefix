# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
# get_loc and get_value should treat datetime objects symmetrically
# TODO: this test used to test get_value, which is removed in 2.0.
#  should this test be moved somewhere, or is what's left redundant?
dti = date_range("2016-01-01", periods=3, freq="MS")
pi = dti.to_period(freq)
ser = Series(range(7, 10), index=pi)

ts = dti[0]

assert pi.get_loc(ts) == 0
assert ser[ts] == 7
assert ser.loc[ts] == 7

ts2 = ts + Timedelta(hours=3)
if freq == "H":
    with pytest.raises(KeyError, match="2016-01-01 03:00"):
        pi.get_loc(ts2)
    with pytest.raises(KeyError, match="2016-01-01 03:00"):
        ser[ts2]
    with pytest.raises(KeyError, match="2016-01-01 03:00"):
        ser.loc[ts2]
else:
    assert pi.get_loc(ts2) == 0
    assert ser[ts2] == 7
    assert ser.loc[ts2] == 7
