# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py
exit(self._index.groupby(Categorical.from_codes(self.codes, self.group_index)))
