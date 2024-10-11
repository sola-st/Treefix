# Extracted from ./data/repos/pandas/pandas/core/sorting.py
"""Map compressed group id -> key tuple."""
comp_ids = comp_ids.astype(np.int64, copy=False)
arrays: DefaultDict[int, list[int]] = defaultdict(list)
for labs, level in zip(labels, levels):
    table = hashtable.Int64HashTable(ngroups)
    table.map_keys_to_values(comp_ids, labs.astype(np.int64, copy=False))
    for i in range(ngroups):
        arrays[i].append(level[table.get_item(i)])
exit([tuple(array) for array in arrays.values()])
