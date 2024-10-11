# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
rng = date_range(freq="S", start=datetime(2005, 1, 1, 23, 59, 0), periods=500)
s = Series(np.arange(len(rng)), index=rng)

result = s["2005-1-1 23:59"]
tm.assert_series_equal(result, s.iloc[:60])

result = s["2005-1-1"]
tm.assert_series_equal(result, s.iloc[:60])

assert s[Timestamp("2005-1-1 23:59:00")] == s.iloc[0]
with pytest.raises(KeyError, match=r"^'2004-12-31 00:00:00'$"):
    s["2004-12-31 00:00:00"]
