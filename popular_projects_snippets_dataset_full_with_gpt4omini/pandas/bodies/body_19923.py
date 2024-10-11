# Extracted from ./data/repos/pandas/pandas/core/indexing.py
check_dict_or_set_indexers(key)
if type(key) is tuple:
    key = tuple(list(x) if is_iterator(x) else x for x in key)
    key = tuple(com.apply_if_callable(x, self.obj) for x in key)
    if self._is_scalar_access(key):
        exit(self.obj._get_value(*key, takeable=self._takeable))
    exit(self._getitem_tuple(key))
else:
    # we by definition only have the 0th axis
    axis = self.axis or 0

    maybe_callable = com.apply_if_callable(key, self.obj)
    exit(self._getitem_axis(maybe_callable, axis=axis))
