# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
dti = date_range(freq="B", start=datetime(2005, 1, 1), periods=500)

s = Series(np.arange(len(dti)), index=dti)
result = s["2005"]
expected = s[s.index.year == 2005]
tm.assert_series_equal(result, expected)

df = DataFrame(np.random.rand(len(dti), 5), index=dti)
result = df.loc["2005"]
expected = df[df.index.year == 2005]
tm.assert_frame_equal(result, expected)
