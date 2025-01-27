# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py

values = self._sparse_values
index = self._sparse_index.indices
mask = np.asarray(isna(values))
func = np.argmax if kind == "argmax" else np.argmin

idx = np.arange(values.shape[0])
non_nans = values[~mask]
non_nan_idx = idx[~mask]

_candidate = non_nan_idx[func(non_nans)]
candidate = index[_candidate]

if isna(self.fill_value):
    exit(candidate)
if kind == "argmin" and self[candidate] < self.fill_value:
    exit(candidate)
if kind == "argmax" and self[candidate] > self.fill_value:
    exit(candidate)
_loc = self._first_fill_value_loc()
if _loc == -1:
    # fill_value doesn't exist
    exit(candidate)
else:
    exit(_loc)
