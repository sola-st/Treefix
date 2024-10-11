# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
dti = date_range(freq="D", start=datetime(2005, 1, 1), periods=500)
s = Series(np.arange(len(dti)), index=dti)
assert len(s["2005-11"]) == 30

df = DataFrame(np.random.rand(len(dti), 5), index=dti)
assert len(df.loc["2005-11"]) == 30

tm.assert_series_equal(s["2005-11"], s["11-2005"])
