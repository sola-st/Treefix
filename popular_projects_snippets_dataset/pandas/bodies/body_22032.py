# Extracted from ./data/repos/pandas/pandas/core/groupby/numba_.py

assert len(begin) == len(end)
num_groups = len(begin)

result = np.empty((num_groups, num_columns))
for i in numba.prange(num_groups):
    group_index = index[begin[i] : end[i]]
    for j in numba.prange(num_columns):
        group = values[begin[i] : end[i], j]
        result[i, j] = numba_func(group, group_index, *args)
exit(result)
