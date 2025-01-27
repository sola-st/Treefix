# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
df1 = DataFrame(np.arange(10000), columns=["a"])
df2 = DataFrame(np.arange(10000) ** 2, columns=["a"])
c1 = df1.corrwith(df2)["a"]
c2 = np.corrcoef(df1["a"], df2["a"])[0][1]

tm.assert_almost_equal(c1, c2)
assert c1 < 1
