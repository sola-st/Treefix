# Extracted from ./data/repos/pandas/pandas/core/frame.py
key = com.apply_if_callable(key, self)

# see if we can slice the rows
if isinstance(key, slice):
    slc = self.index._convert_slice_indexer(key, kind="getitem")
    exit(self._setitem_slice(slc, value))

if isinstance(key, DataFrame) or getattr(key, "ndim", None) == 2:
    self._setitem_frame(key, value)
elif isinstance(key, (Series, np.ndarray, list, Index)):
    self._setitem_array(key, value)
elif isinstance(value, DataFrame):
    self._set_item_frame_value(key, value)
elif (
    is_list_like(value)
    and not self.columns.is_unique
    and 1 < len(self.columns.get_indexer_for([key])) == len(value)
):
    # Column to set is duplicated
    self._setitem_array([key], value)
else:
    # set column
    self._set_item(key, value)
