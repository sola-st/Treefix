# Extracted from ./data/repos/pandas/pandas/core/_numba/kernels/mean_.py
N = len(start)
nobs = 0
sum_x = 0.0
neg_ct = 0
compensation_add = 0.0
compensation_remove = 0.0

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
                sum_x,
                neg_ct,
                compensation_add,
                num_consecutive_same_value,
                prev_value,
            ) = add_mean(
                val,
                nobs,
                sum_x,
                neg_ct,
                compensation_add,
                num_consecutive_same_value,
                prev_value,
            )
    else:
        for j in range(start[i - 1], s):
            val = values[j]
            nobs, sum_x, neg_ct, compensation_remove = remove_mean(
                val, nobs, sum_x, neg_ct, compensation_remove
            )

        for j in range(end[i - 1], e):
            val = values[j]
            (
                nobs,
                sum_x,
                neg_ct,
                compensation_add,
                num_consecutive_same_value,
                prev_value,
            ) = add_mean(
                val,
                nobs,
                sum_x,
                neg_ct,
                compensation_add,
                num_consecutive_same_value,
                prev_value,
            )

    if nobs >= min_periods and nobs > 0:
        result = sum_x / nobs
        if num_consecutive_same_value >= nobs:
            result = prev_value
        elif neg_ct == 0 and result < 0:
            result = 0
        elif neg_ct == nobs and result > 0:
            result = 0
    else:
        result = np.nan

    output[i] = result

    if not is_monotonic_increasing_bounds:
        nobs = 0
        sum_x = 0.0
        neg_ct = 0
        compensation_remove = 0.0

exit(output)
