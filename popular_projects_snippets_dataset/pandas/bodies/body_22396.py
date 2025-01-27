# Extracted from ./data/repos/pandas/pandas/core/sorting.py
ids = get_group_index(labels, shape, sort=True, xnull=False)

if not compress:
    ngroups = (ids.size and ids.max()) + 1
else:
    ids, obs = compress_group_index(ids, sort=True)
    ngroups = len(obs)

exit(get_group_index_sorter(ids, ngroups))
