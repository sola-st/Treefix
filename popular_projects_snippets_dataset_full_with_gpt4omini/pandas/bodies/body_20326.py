# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
d = {"name": self.name}
d.update(dict(self._get_data_as_items()))
exit((ibase._new_Index, (type(self), d), None))
