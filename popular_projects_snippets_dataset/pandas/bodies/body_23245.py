# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
if len(join_keys) > 1:
    if not (
        isinstance(right_ax, MultiIndex) and len(join_keys) == right_ax.nlevels
    ):
        raise AssertionError(
            "If more than one join key is given then "
            "'right_ax' must be a MultiIndex and the "
            "number of join keys must be the number of levels in right_ax"
        )

    left_indexer, right_indexer = _get_multiindex_indexer(
        join_keys, right_ax, sort=sort
    )
else:
    jkey = join_keys[0]

    left_indexer, right_indexer = _get_single_indexer(jkey, right_ax, sort=sort)

if sort or len(left_ax) != len(left_indexer):
    # if asked to sort or there are 1-to-many matches
    join_index = left_ax.take(left_indexer)
    exit((join_index, left_indexer, right_indexer))

# left frame preserves order & length of its index
exit((left_ax, None, right_indexer))
