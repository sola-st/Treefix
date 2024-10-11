# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
arr = self._data
mask = self._mask

# Use a sentinel for na; recode and add NA to uniques if necessary below
codes, uniques = factorize_array(arr, use_na_sentinel=True, mask=mask)

# check that factorize_array correctly preserves dtype.
assert uniques.dtype == self.dtype.numpy_dtype, (uniques.dtype, self.dtype)

has_na = mask.any()
if use_na_sentinel or not has_na:
    size = len(uniques)
else:
    # Make room for an NA value
    size = len(uniques) + 1
uniques_mask = np.zeros(size, dtype=bool)
if not use_na_sentinel and has_na:
    na_index = mask.argmax()
    # Insert na with the proper code
    if na_index == 0:
        na_code = np.intp(0)
    else:
        # mypy error: Slice index must be an integer or None
        # https://github.com/python/mypy/issues/2410
        na_code = codes[:na_index].max() + 1  # type: ignore[misc]
    codes[codes >= na_code] += 1
    codes[codes == -1] = na_code
    # dummy value for uniques; not used since uniques_mask will be True
    uniques = np.insert(uniques, na_code, 0)
    uniques_mask[na_code] = True
uniques_ea = type(self)(uniques, uniques_mask)

exit((codes, uniques_ea))
