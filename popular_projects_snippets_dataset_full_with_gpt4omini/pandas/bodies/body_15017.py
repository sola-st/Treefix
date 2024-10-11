# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
df = hist_df
axes = df.height.hist(by=df.gender)  # noqa
assert len(self.plt.get_fignums()) == 1
