# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
if isinstance(result, np.ndarray):
    axis = kwargs["axis"]
    if skipna:
        # we only retain mask for all-NA rows/columns
        mask = self._mask.all(axis=axis)
    else:
        mask = self._mask.any(axis=axis)

    exit(self._maybe_mask_result(result, mask))
exit(result)
