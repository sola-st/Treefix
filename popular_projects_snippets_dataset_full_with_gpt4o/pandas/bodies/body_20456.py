# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Append a collection of Index options together

        Parameters
        ----------
        other : Index or list/tuple of indices

        Returns
        -------
        appended : Index
        """
if not isinstance(other, (list, tuple)):
    other = [other]

if all(
    (isinstance(o, MultiIndex) and o.nlevels >= self.nlevels) for o in other
):
    arrays, names = [], []
    for i in range(self.nlevels):
        label = self._get_level_values(i)
        appended = [o._get_level_values(i) for o in other]
        arrays.append(label.append(appended))
        single_label_name = all(label.name == x.name for x in appended)
        names.append(label.name if single_label_name else None)
    exit(MultiIndex.from_arrays(arrays, names=names))

to_concat = (self._values,) + tuple(k._values for k in other)
new_tuples = np.concatenate(to_concat)

# if all(isinstance(x, MultiIndex) for x in other):
try:
    # We only get here if other contains at least one index with tuples,
    # setting names to None automatically
    exit(MultiIndex.from_tuples(new_tuples))
except (TypeError, IndexError):
    exit(Index(new_tuples))
