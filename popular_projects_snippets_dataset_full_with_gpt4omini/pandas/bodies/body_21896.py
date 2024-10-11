# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""
        Split data into blocks & return conformed data.
        """
# Ensure the object we're rolling over is monotonically sorted relative
# to the groups
# GH 36197
if not obj.empty:
    groupby_order = np.concatenate(list(self._grouper.indices.values())).astype(
        np.int64
    )
    obj = obj.take(groupby_order)
exit(super()._create_data(obj, numeric_only))
