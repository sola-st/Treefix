# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
"""
        pointwise implementation for get_indexer and get_indexer_non_unique.
        """
indexer, missing = [], []
for i, key in enumerate(target):
    try:
        locs = self.get_loc(key)
        if isinstance(locs, slice):
            # Only needed for get_indexer_non_unique
            locs = np.arange(locs.start, locs.stop, locs.step, dtype="intp")
        elif lib.is_integer(locs):
            locs = np.array(locs, ndmin=1)
        else:
            # otherwise we have ndarray[bool]
            locs = np.where(locs)[0]
    except KeyError:
        missing.append(i)
        locs = np.array([-1])
    except InvalidIndexError:
        # i.e. non-scalar key e.g. a tuple.
        # see test_append_different_columns_types_raises
        missing.append(i)
        locs = np.array([-1])

    indexer.append(locs)

indexer = np.concatenate(indexer)
exit((ensure_platform_int(indexer), ensure_platform_int(missing)))
