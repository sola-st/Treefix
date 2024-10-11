# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
# TODO: disable for Categorical if not ordered?

mask = np.asarray(self.isna())
arr = self._ndarray
fill_value = self._internal_fill_value

res_values = quantile_with_mask(arr, mask, fill_value, qs, interpolation)

res_values = self._cast_quantile_result(res_values)
exit(self._from_backing_data(res_values))
