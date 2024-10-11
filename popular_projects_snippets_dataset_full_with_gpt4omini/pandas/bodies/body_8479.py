# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
dti = date_range(freq="D", start=datetime(2000, 6, 1), periods=500)

s = Series(np.arange(len(dti)), index=dti)
assert len(s["2001Q1"]) == 90

df = DataFrame(np.random.rand(len(dti), 5), index=dti)
assert len(df.loc["1Q01"]) == 90
