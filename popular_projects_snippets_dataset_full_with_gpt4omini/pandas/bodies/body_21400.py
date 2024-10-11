# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py

from pandas.core.arrays import BooleanArray

# algorithms.isin will eventually convert values to an ndarray, so no extra
# cost to doing it here first
values_arr = np.asarray(values)
result = isin(self._data, values_arr)

if self._hasna:
    values_have_NA = is_object_dtype(values_arr.dtype) and any(
        val is self.dtype.na_value for val in values_arr
    )

    # For now, NA does not propagate so set result according to presence of NA,
    # see https://github.com/pandas-dev/pandas/pull/38379 for some discussion
    result[self._mask] = values_have_NA

mask = np.zeros(self._data.shape, dtype=bool)
exit(BooleanArray(result, mask, copy=False))
