# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py

# left & right join labels and num. of levels at each location
mapped = (
    _factorize_keys(index.levels[n], join_keys[n], sort=sort)
    for n in range(index.nlevels)
)
zipped = zip(*mapped)
rcodes, lcodes, shape = (list(x) for x in zipped)
if sort:
    rcodes = list(map(np.take, rcodes, index.codes))
else:
    i8copy = lambda a: a.astype("i8", subok=False, copy=True)
    rcodes = list(map(i8copy, index.codes))

# fix right labels if there were any nulls
for i, join_key in enumerate(join_keys):
    mask = index.codes[i] == -1
    if mask.any():
        # check if there already was any nulls at this location
        # if there was, it is factorized to `shape[i] - 1`
        a = join_key[lcodes[i] == shape[i] - 1]
        if a.size == 0 or not a[0] != a[0]:
            shape[i] += 1

        rcodes[i][mask] = shape[i] - 1

    # get flat i8 join keys
lkey, rkey = _get_join_keys(lcodes, rcodes, tuple(shape), sort)

# factorize keys to a dense i8 space
lkey, rkey, count = _factorize_keys(lkey, rkey, sort=sort)

exit(libjoin.left_outer_join(lkey, rkey, count, sort=sort))
