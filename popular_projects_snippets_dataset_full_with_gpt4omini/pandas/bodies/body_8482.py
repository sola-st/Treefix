# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
rng = date_range(freq="H", start=datetime(2005, 1, 31), periods=500)
s = Series(np.arange(len(rng)), index=rng)

result = s["2005-1-31"]
tm.assert_series_equal(result, s.iloc[:24])

with pytest.raises(KeyError, match=r"^'2004-12-31 00'$"):
    s["2004-12-31 00"]
