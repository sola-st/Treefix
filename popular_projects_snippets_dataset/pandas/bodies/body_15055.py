# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_groupby.py
n = 10
weight = Series(np.random.normal(166, 20, size=n))
height = Series(np.random.normal(60, 10, size=n))
with tm.RNGContext(42):
    gender = np.random.choice(["male", "female"], size=n)

weight.groupby(gender).plot()
tm.close()
height.groupby(gender).hist()
tm.close()
# Regression test for GH8733
height.groupby(gender).plot(alpha=0.5)
tm.close()
