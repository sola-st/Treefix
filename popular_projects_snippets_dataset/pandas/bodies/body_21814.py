# Extracted from ./data/repos/pandas/pandas/core/window/numba_.py
alpha = 1.0 / (1.0 + com)
old_wt_factor = 1.0 - alpha
new_wt = 1.0 if adjust else alpha
old_wt = np.ones(values.shape[1])

result = np.empty(values.shape)
weighted = values[0].copy()
nobs = (~np.isnan(weighted)).astype(np.int64)
result[0] = np.where(nobs >= minimum_periods, weighted, np.nan)
for i in range(1, len(values)):
    cur = values[i]
    is_observations = ~np.isnan(cur)
    nobs += is_observations.astype(np.int64)
    for j in numba.prange(len(cur)):
        if not np.isnan(weighted[j]):
            if is_observations[j] or not ignore_na:
                if normalize:
                    # note that len(deltas) = len(vals) - 1 and deltas[i]
                    # is to be used in conjunction with vals[i+1]
                    old_wt[j] *= old_wt_factor ** deltas[i - 1]
                else:
                    weighted[j] = old_wt_factor * weighted[j]
                if is_observations[j]:
                    if normalize:
                        # avoid numerical errors on constant series
                        if weighted[j] != cur[j]:
                            weighted[j] = (
                                old_wt[j] * weighted[j] + new_wt * cur[j]
                            )
                            if normalize:
                                weighted[j] = weighted[j] / (old_wt[j] + new_wt)
                        if adjust:
                            old_wt[j] += new_wt
                        else:
                            old_wt[j] = 1.0
                    else:
                        weighted[j] += cur[j]
        elif is_observations[j]:
            weighted[j] = cur[j]

    result[i] = np.where(nobs >= minimum_periods, weighted, np.nan)

exit(result)
