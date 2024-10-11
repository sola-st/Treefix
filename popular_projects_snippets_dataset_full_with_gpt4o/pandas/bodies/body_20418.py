# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
names = name if name is not lib.no_default else self.names

exit(type(self).from_tuples(values, sortorder=None, names=names))
