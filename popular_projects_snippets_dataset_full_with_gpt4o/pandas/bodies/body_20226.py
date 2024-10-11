# Extracted from ./data/repos/pandas/pandas/core/_numba/kernels/var_.py
N = len(start)
nobs = 0
mean_x = 0.0
ssqdm_x = 0.0
compensation_add = 0.0
compensation_remove = 0.0

min_periods = max(min_periods, 1)
is_monotonic_increasing_bounds = is_monotonic_increasing(
    start
) and is_monotonic_increasing(end)

output = np.empty(N, dtype=np.float64)

for i in range(N):
    s = start[i]
    e = end[i]
    if i == 0 or not is_monotonic_increasing_bounds:

        prev_value = values[s]
        num_consecutive_same_value = 0

        for j in range(s, e):
            val = values[j]
            (
                nobs,
                mean_x,
                ssqdm_x,
                compensation_add,
                num_consecutive_same_value,
                prev_value,
            ) = add_var(
                val,
                nobs,
                mean_x,
                ssqdm_x,
                compensation_add,
                num_consecutive_same_value,
                prev_value,
            )
    else:
        for j in range(start[i - 1], s):
            val = values[j]
            nobs, mean_x, ssqdm_x, compensation_remove = remove_var(
                val, nobs, mean_x, ssqdm_x, compensation_remove
            )

        for j in range(end[i - 1], e):
            val = values[j]
            (
                nobs,
                mean_x,
                ssqdm_x,
                compensation_add,
                num_consecutive_same_value,
                prev_value,
            ) = add_var(
                val,
                nobs,
                mean_x,
                ssqdm_x,
                compensation_add,
                num_consecutive_same_value,
                prev_value,
            )

    if nobs >= min_periods and nobs > ddof:
        if nobs == 1 or num_consecutive_same_value >= nobs:
            result = 0.0
        else:
            result = ssqdm_x / (nobs - ddof)
    else:
        result = np.nan

    output[i] = result

    if not is_monotonic_increasing_bounds:
        nobs = 0
        mean_x = 0.0
        ssqdm_x = 0.0
        compensation_remove = 0.0

exit(output)
