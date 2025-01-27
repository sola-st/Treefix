# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""Check if we do need a multi reindex."""
exit((
    (common.count_not_none(*axes.values()) == self._AXIS_LEN)
    and method is None
    and level is None
    and not self._is_mixed_type
    and not (
        self.ndim == 2
        and len(self.dtypes) == 1
        and is_extension_array_dtype(self.dtypes.iloc[0])
    )
))
