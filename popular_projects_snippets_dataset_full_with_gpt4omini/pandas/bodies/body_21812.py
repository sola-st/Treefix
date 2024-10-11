# Extracted from ./data/repos/pandas/pandas/core/window/numba_.py
result = np.empty(table.shape[1])
for i in numba.prange(table.shape[1]):
    partition = table[:, i]
    result[i] = nan_func(partition)
exit(result)
