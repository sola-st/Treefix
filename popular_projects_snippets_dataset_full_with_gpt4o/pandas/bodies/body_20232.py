# Extracted from ./data/repos/pandas/pandas/core/_numba/executor.py
result = np.empty((len(start), values.shape[1]), dtype=np.float64)
for i in numba.prange(values.shape[1]):
    result[:, i] = func(values[:, i], start, end, min_periods, *args)
exit(result)
