# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH4377 df.to_json segfaults with non-ndarray blocks
df = DataFrame(np.random.randn(10, 4))
df.loc[:8] = np.nan

sdf = df.astype("Sparse")
expected = df.to_json()
assert expected == sdf.to_json()

s = Series(np.random.randn(10))
s.loc[:8] = np.nan
ss = s.astype("Sparse")

expected = s.to_json()
assert expected == ss.to_json()
