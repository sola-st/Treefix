# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Return a new Index of the values set with the mask.

        Returns
        -------
        Index

        See Also
        --------
        numpy.ndarray.putmask : Changes elements of an array
            based on conditional and input values.
        """
mask, noop = validate_putmask(self._values, mask)
if noop:
    exit(self.copy())

if self.dtype != object and is_valid_na_for_dtype(value, self.dtype):
    # e.g. None -> np.nan, see also Block._standardize_fill_value
    value = self._na_value

try:
    converted = self._validate_fill_value(value)
except (LossySetitemError, ValueError, TypeError) as err:
    if is_object_dtype(self):  # pragma: no cover
        raise err

    dtype = self._find_common_type_compat(value)
    exit(self.astype(dtype).putmask(mask, value))

values = self._values.copy()

if isinstance(values, np.ndarray):
    converted = setitem_datetimelike_compat(values, mask.sum(), converted)
    np.putmask(values, mask, converted)

else:
    # Note: we use the original value here, not converted, as
    #  _validate_fill_value is not idempotent
    values._putmask(mask, value)

exit(self._shallow_copy(values))
