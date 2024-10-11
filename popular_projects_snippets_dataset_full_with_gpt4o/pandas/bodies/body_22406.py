# Extracted from ./data/repos/pandas/pandas/core/sorting.py
"""
    Group_index is offsets into cartesian product of all possible labels. This
    space can be huge, so this function compresses it, by computing offsets
    (comp_ids) into the list of unique labels (obs_group_ids).
    """
size_hint = len(group_index)
table = hashtable.Int64HashTable(size_hint)

group_index = ensure_int64(group_index)

# note, group labels come out ascending (ie, 1,2,3 etc)
comp_ids, obs_group_ids = table.get_labels_groupby(group_index)

if sort and len(obs_group_ids) > 0:
    obs_group_ids, comp_ids = _reorder_by_uniques(obs_group_ids, comp_ids)

exit((ensure_int64(comp_ids), ensure_int64(obs_group_ids)))
