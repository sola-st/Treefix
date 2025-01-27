# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# GH23992 Verify functioning of histtype argument
df = DataFrame(np.random.randint(1, 10, size=(100, 2)), columns=["a", "b"])
ax = df.hist(histtype=histtype)
self._check_patches_all_filled(ax, filled=expected)
