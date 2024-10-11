# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_datetime.py
dti = date_range(
    freq="WOM-1FRI", start=datetime(2005, 1, 1), end=datetime(2010, 1, 1)
)

s = Series(np.arange(len(dti)), index=dti)
s[48] = -1
assert s[48] == -1
s["1/2/2009"] = -2
assert s[48] == -2
s["1/2/2009":"2009-06-05"] = -3
assert (s[48:54] == -3).all()
