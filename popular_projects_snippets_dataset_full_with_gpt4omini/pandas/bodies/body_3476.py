# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# see gh-10174

# interpolation = linear (default case)
df = datetime_frame
q = df.quantile(0.1, axis=0, numeric_only=True, interpolation="linear")
assert q["A"] == np.percentile(df["A"], 10)
