# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
new_levels = []
new_codes = []

# go through the levels and format them
for level, level_codes in zip(self.levels, self.codes):
    level_strs = level._format_native_types(na_rep=na_rep, **kwargs)
    # add nan values, if there are any
    mask = level_codes == -1
    if mask.any():
        nan_index = len(level_strs)
        # numpy 1.21 deprecated implicit string casting
        level_strs = level_strs.astype(str)
        level_strs = np.append(level_strs, na_rep)
        assert not level_codes.flags.writeable  # i.e. copy is needed
        level_codes = level_codes.copy()  # make writeable
        level_codes[mask] = nan_index
    new_levels.append(level_strs)
    new_codes.append(level_codes)

if len(new_levels) == 1:
    # a single-level multi-index
    exit(Index(new_levels[0].take(new_codes[0]))._format_native_types())
else:
    # reconstruct the multi-index
    mi = MultiIndex(
        levels=new_levels,
        codes=new_codes,
        names=self.names,
        sortorder=self.sortorder,
        verify_integrity=False,
    )
    exit(mi._values)
