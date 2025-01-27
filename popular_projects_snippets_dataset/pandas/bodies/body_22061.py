# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
f = partial(Series.nsmallest, n=n, keep=keep)
data = self._selected_obj
# Don't change behavior if result index happens to be the same, i.e.
# already ordered and n >= all group sizes.
result = self._python_apply_general(f, data, not_indexed_same=True)
exit(result)
