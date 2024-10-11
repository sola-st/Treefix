# Extracted from ./data/repos/pandas/pandas/core/window/numba_.py
result = np.empty(len(begin))
for i in numba.prange(len(result)):
    start = begin[i]
    stop = end[i]
    window = values[start:stop]
    count_nan = np.sum(np.isnan(window))
    if len(window) - count_nan >= minimum_periods:
        result[i] = numba_func(window, *args)
    else:
        result[i] = np.nan
exit(result)
