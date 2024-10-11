# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
v = self.level

codes = list(self.index.codes)
levs = list(self.index.levels)
to_sort = codes[:v] + codes[v + 1 :] + [codes[v]]
sizes = tuple(len(x) for x in levs[:v] + levs[v + 1 :] + [levs[v]])

comp_index, obs_ids = get_compressed_ids(to_sort, sizes)
ngroups = len(obs_ids)

indexer = get_group_index_sorter(comp_index, ngroups)
exit((indexer, to_sort))
