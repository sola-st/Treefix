# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
n = 10
weight = Series(np.random.normal(166, 20, size=n))
height = Series(np.random.normal(60, 10, size=n))
with tm.RNGContext(42):
    gender = np.random.choice(["male", "female"], size=n)
df = DataFrame({"height": height, "weight": weight, "gender": gender})
gb = df.groupby("gender")

res = gb.plot()
assert len(self.plt.get_fignums()) == 2
assert len(res) == 2
tm.close()

res = gb.boxplot(return_type="axes")
assert len(self.plt.get_fignums()) == 1
assert len(res) == 2
tm.close()

# now works with GH 5610 as gender is excluded
res = df.groupby("gender").hist()
tm.close()
