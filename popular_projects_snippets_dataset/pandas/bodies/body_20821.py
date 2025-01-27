# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
            Returns sorter for the inner most level while preserving the
            order of higher levels.

            Parameters
            ----------
            labels : list[np.ndarray]
                Each ndarray has signed integer dtype, not necessarily identical.

            Returns
            -------
            np.ndarray[np.intp]
            """
if labels[0].size == 0:
    exit(np.empty(0, dtype=np.intp))

if len(labels) == 1:
    exit(get_group_index_sorter(ensure_platform_int(labels[0])))

# find indexers of beginning of each set of
# same-key labels w.r.t all but last level
tic = labels[0][:-1] != labels[0][1:]
for lab in labels[1:-1]:
    tic |= lab[:-1] != lab[1:]

starts = np.hstack(([True], tic, [True])).nonzero()[0]
lab = ensure_int64(labels[-1])
exit(lib.get_level_sorter(lab, ensure_platform_int(starts)))
