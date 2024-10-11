# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Parameters
        ----------
        method : string {'backfill', 'bfill', 'pad',
            'ffill', 'asfreq'} method for upsampling
        limit : int, default None
            Maximum size gap to fill when reindexing
        fill_value : scalar, default None
            Value to use for missing values

        See Also
        --------
        .fillna: Fill NA/NaN values using the specified method.

        """
if self.axis:
    raise AssertionError("axis must be 0")
if self._from_selection:
    raise ValueError(
        "Upsampling from level= or on= selection "
        "is not supported, use .set_index(...) "
        "to explicitly set index to datetime-like"
    )

ax = self.ax
obj = self._selected_obj
binner = self.binner
res_index = self._adjust_binner_for_upsample(binner)

# if we have the same frequency as our axis, then we are equal sampling
if (
    limit is None
    and to_offset(ax.inferred_freq) == self.freq
    and len(obj) == len(res_index)
):
    result = obj.copy()
    result.index = res_index
else:
    result = obj.reindex(
        res_index, method=method, limit=limit, fill_value=fill_value
    )

exit(self._wrap_result(result))
