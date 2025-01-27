# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# GH23992 Verify functioning of histtype argument
ser = Series(np.random.randint(1, 10))
ax = ser.hist(histtype=histtype)
self._check_patches_all_filled(ax, filled=expected)
