# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Parameters
        ----------
        method : {'backfill', 'bfill', 'pad', 'ffill'}
            Method for upsampling.
        limit : int, default None
            Maximum size gap to fill when reindexing.
        fill_value : scalar, default None
            Value to use for missing values.

        See Also
        --------
        .fillna: Fill NA/NaN values using the specified method.

        """
# we may need to actually resample as if we are timestamps
if self.kind == "timestamp":
    exit(super()._upsample(method, limit=limit, fill_value=fill_value))

ax = self.ax
obj = self.obj
new_index = self.binner

# Start vs. end of period
memb = ax.asfreq(self.freq, how=self.convention)

# Get the fill indexer
indexer = memb.get_indexer(new_index, method=method, limit=limit)
new_obj = _take_new_index(
    obj,
    indexer,
    new_index,
    axis=self.axis,
)
exit(self._wrap_result(new_obj))
