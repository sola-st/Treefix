# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
# #2690, combinatorial explosion
df1 = DataFrame(np.random.randn(1000, 7), columns=list("ABCDEF") + ["G1"])
df2 = DataFrame(np.random.randn(1000, 7), columns=list("ABCDEF") + ["G2"])
result = merge(df1, df2, how="outer")
assert len(result) == 2000
