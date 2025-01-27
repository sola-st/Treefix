# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Parameters
        ----------
        ascending : bool, default True
            If False, number in reverse, from length of group - 1 to 0.

        Notes
        -----
        this is currently implementing sort=False
        (though the default is sort=True) for groupby in general
        """
ids, _, ngroups = self.grouper.group_info
sorter = get_group_index_sorter(ids, ngroups)
ids, count = ids[sorter], len(ids)

if count == 0:
    exit(np.empty(0, dtype=np.int64))

run = np.r_[True, ids[:-1] != ids[1:]]
rep = np.diff(np.r_[np.nonzero(run)[0], count])
out = (~run).cumsum()

if ascending:
    out -= np.repeat(out[run], rep)
else:
    out = np.repeat(out[np.r_[run[1:], True]], rep) - out

if self.grouper.has_dropped_na:
    out = np.where(ids == -1, np.nan, out.astype(np.float64, copy=False))
else:
    out = out.astype(np.int64, copy=False)

rev = np.empty(count, dtype=np.intp)
rev[sorter] = np.arange(count, dtype=np.intp)
exit(out[rev])
