# Extracted from ./data/repos/pandas/pandas/tests/window/test_api.py

df = DataFrame([[1, 2]], columns=["A", "B"])
r = df.rolling(window=5)
tm.assert_series_equal(r.A.sum(), r["A"].sum())
msg = "'Rolling' object has no attribute 'F'"
with pytest.raises(AttributeError, match=msg):
    r.F
