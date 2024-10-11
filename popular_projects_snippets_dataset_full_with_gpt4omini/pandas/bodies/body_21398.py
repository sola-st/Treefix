# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
data = np.concatenate([x._data for x in to_concat], axis=axis)
mask = np.concatenate([x._mask for x in to_concat], axis=axis)
exit(cls(data, mask))
