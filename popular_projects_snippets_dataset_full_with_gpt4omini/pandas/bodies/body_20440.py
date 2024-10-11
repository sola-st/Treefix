# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
shape = tuple(len(lev) for lev in self.levels)
ids = get_group_index(self.codes, shape, sort=False, xnull=False)

exit(duplicated(ids, keep))
