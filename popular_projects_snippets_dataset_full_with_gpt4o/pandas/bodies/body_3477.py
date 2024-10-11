# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# see gh-10174

df = int_frame
# interpolation = linear (default case)
q = df.quantile(0.1)
assert q["A"] == np.percentile(df["A"], 10)

# test with and without interpolation keyword
q1 = df.quantile(0.1, axis=0, interpolation="linear")
assert q1["A"] == np.percentile(df["A"], 10)
tm.assert_series_equal(q, q1)
