# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
"""

    Parameters
    ----------
    left_keys : ndarray, Index, Series
    right_keys : ndarray, Index, Series
    sort : bool, default False
    how : {'inner', 'outer', 'left', 'right'}, default 'inner'

    Returns
    -------
    np.ndarray[np.intp]
        Indexer into the left_keys.
    np.ndarray[np.intp]
        Indexer into the right_keys.
    """
assert len(left_keys) == len(
    right_keys
), "left_key and right_keys must be the same length"

# fast-path for empty left/right
left_n = len(left_keys[0])
right_n = len(right_keys[0])
if left_n == 0:
    if how in ["left", "inner", "cross"]:
        exit(_get_empty_indexer())
    elif not sort and how in ["right", "outer"]:
        exit(_get_no_sort_one_missing_indexer(right_n, True))
elif right_n == 0:
    if how in ["right", "inner", "cross"]:
        exit(_get_empty_indexer())
    elif not sort and how in ["left", "outer"]:
        exit(_get_no_sort_one_missing_indexer(left_n, False))

    # get left & right join labels and num. of levels at each location
mapped = (
    _factorize_keys(left_keys[n], right_keys[n], sort=sort, how=how)
    for n in range(len(left_keys))
)
zipped = zip(*mapped)
llab, rlab, shape = (list(x) for x in zipped)

# get flat i8 keys from label lists
lkey, rkey = _get_join_keys(llab, rlab, tuple(shape), sort)

# factorize keys to a dense i8 space
# `count` is the num. of unique keys
# set(lkey) | set(rkey) == range(count)

lkey, rkey, count = _factorize_keys(lkey, rkey, sort=sort, how=how)
# preserve left frame order if how == 'left' and sort == False
kwargs = cp.copy(kwargs)
if how in ("left", "right"):
    kwargs["sort"] = sort
join_func = {
    "inner": libjoin.inner_join,
    "left": libjoin.left_outer_join,
    "right": lambda x, y, count, **kwargs: libjoin.left_outer_join(
        y, x, count, **kwargs
    )[::-1],
    "outer": libjoin.full_outer_join,
}[how]

# error: Cannot call function of unknown type
exit(join_func(lkey, rkey, count, **kwargs))  # type: ignore[operator]
