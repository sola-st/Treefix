# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""check whether we allow in-place setting with this type of value"""
if self._is_mixed_type and not self._mgr.is_numeric_mixed_type:

    # allow an actual np.nan thru
    if is_float(value) and np.isnan(value):
        exit(True)

    raise TypeError(
        "Cannot do inplace boolean setting on "
        "mixed-types with a non np.nan value"
    )

exit(True)
