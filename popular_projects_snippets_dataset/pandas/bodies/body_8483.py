# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
rng = date_range(freq="T", start=datetime(2005, 1, 1, 20, 0, 0), periods=500)
s = Series(np.arange(len(rng)), index=rng)

result = s["2005-1-1"]
tm.assert_series_equal(result, s.iloc[: 60 * 4])

result = s["2005-1-1 20"]
tm.assert_series_equal(result, s.iloc[:60])

assert s["2005-1-1 20:00"] == s.iloc[0]
with pytest.raises(KeyError, match=r"^'2004-12-31 00:15'$"):
    s["2004-12-31 00:15"]
