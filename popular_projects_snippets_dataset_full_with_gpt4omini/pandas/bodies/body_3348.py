# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# gh 3907
df = DataFrame([["foo", "bar", "bah"], ["bar", "foo", "bah"]])
m = {"foo": 1, "bar": 2, "bah": 3}
rep = df.replace(m)
expec = Series([np.int64] * 3)
res = rep.dtypes
tm.assert_series_equal(expec, res)
