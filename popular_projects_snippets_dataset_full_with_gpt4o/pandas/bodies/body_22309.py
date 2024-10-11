# Extracted from ./data/repos/pandas/pandas/core/resample.py
result = self._downsample("count")
if not len(self.ax):
    if self._selected_obj.ndim == 1:
        result = type(self._selected_obj)(
            [], index=result.index, dtype="int64", name=self._selected_obj.name
        )
    else:
        from pandas import DataFrame

        result = DataFrame(
            [], index=result.index, columns=result.columns, dtype="int64"
        )

exit(result)
