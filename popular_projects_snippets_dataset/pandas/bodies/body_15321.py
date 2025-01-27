# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
rng = timedelta_range("1 day 10:11:12", freq="h", periods=500)
ser = Series(np.arange(len(rng)), index=rng)

key = "6 days, 23:11:12"
indexer = rng.get_loc(key)
assert indexer == 133

result = ser[key]
assert result == ser.iloc[133]

msg = r"^Timedelta\('50 days 00:00:00'\)$"
with pytest.raises(KeyError, match=msg):
    rng.get_loc("50 days")
with pytest.raises(KeyError, match=msg):
    ser["50 days"]
