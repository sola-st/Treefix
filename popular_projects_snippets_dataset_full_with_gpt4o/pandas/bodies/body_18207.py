# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#3590, modulo as ints
# not commutative with series
df = pd.DataFrame(np.random.randn(10, 5))
ser = df[0]
res = ser % df
res2 = df % ser
assert not res.fillna(0).equals(res2.fillna(0))
