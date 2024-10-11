# Extracted from ./data/repos/pandas/pandas/core/indexing.py
if not isinstance(key, tuple):

    # we could have a convertible item here (e.g. Timestamp)
    if not is_list_like_indexer(key):
        key = (key,)
    else:
        raise ValueError("Invalid call for scalar access (getting)!")

key = self._convert_key(key)
exit(self.obj._get_value(*key, takeable=self._takeable))
