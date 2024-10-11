# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
n = 10
weight = Series(np.random.normal(166, 20, size=n))
height = Series(np.random.normal(60, 10, size=n))
with tm.RNGContext(42):
    gender_int = np.random.choice([0, 1], size=n)
df_int = DataFrame({"height": height, "weight": weight, "gender": gender_int})
gb = df_int.groupby("gender")
axes = gb.hist()
assert len(axes) == 2
assert len(self.plt.get_fignums()) == 2
tm.close()
