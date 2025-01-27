# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
if self._hasna:
    raise ValueError(
        "searchsorted requires array to be sorted, which is impossible "
        "with NAs present."
    )
if isinstance(value, ExtensionArray):
    value = value.astype(object)
# Base class searchsorted would cast to object, which is *much* slower.
exit(self._data.searchsorted(value, side=side, sorter=sorter))
