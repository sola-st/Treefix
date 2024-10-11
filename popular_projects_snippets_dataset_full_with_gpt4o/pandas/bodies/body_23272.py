# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
# We cache this for re-use in ExtensionBlock._unstack
dummy_arr = np.arange(len(self.index), dtype=np.intp)
new_values, mask = self.get_new_values(dummy_arr, fill_value=-1)
exit((new_values, mask.any(0)))
