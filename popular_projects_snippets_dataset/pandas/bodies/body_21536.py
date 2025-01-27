# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
ascending = nv.validate_argsort_with_ascending(ascending, (), kwargs)

if ascending and kind == "quicksort" and na_position == "last":
    # TODO: in an IntervalIndex we can re-use the cached
    #  IntervalTree.left_sorter
    exit(np.lexsort((self.right, self.left)))

# TODO: other cases we can use lexsort for?  much more performant.
exit(super().argsort(
    ascending=ascending, kind=kind, na_position=na_position, **kwargs
))
