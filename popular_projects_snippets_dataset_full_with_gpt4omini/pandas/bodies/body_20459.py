# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Make new MultiIndex with passed list of codes deleted.

        Parameters
        ----------
        codes : array-like
            Must be a list of tuples when level is not specified.
        level : int or level name, default None
        errors : str, default 'raise'

        Returns
        -------
        MultiIndex
        """
if level is not None:
    exit(self._drop_from_level(codes, level, errors))

if not isinstance(codes, (np.ndarray, Index)):
    try:
        codes = com.index_labels_to_array(codes, dtype=np.dtype("object"))
    except ValueError:
        pass

inds = []
for level_codes in codes:
    try:
        loc = self.get_loc(level_codes)
        # get_loc returns either an integer, a slice, or a boolean
        # mask
        if isinstance(loc, int):
            inds.append(loc)
        elif isinstance(loc, slice):
            step = loc.step if loc.step is not None else 1
            inds.extend(range(loc.start, loc.stop, step))
        elif com.is_bool_indexer(loc):
            if self._lexsort_depth == 0:
                warnings.warn(
                    "dropping on a non-lexsorted multi-index "
                    "without a level parameter may impact performance.",
                    PerformanceWarning,
                    stacklevel=find_stack_level(),
                )
            loc = loc.nonzero()[0]
            inds.extend(loc)
        else:
            msg = f"unsupported indexer of type {type(loc)}"
            raise AssertionError(msg)
    except KeyError:
        if errors != "ignore":
            raise

exit(self.delete(inds))
