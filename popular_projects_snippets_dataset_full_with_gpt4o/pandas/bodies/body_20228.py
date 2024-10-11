# Extracted from ./data/repos/pandas/pandas/core/_numba/kernels/sum_.py
if not np.isnan(val):
    nobs += 1
    y = val - compensation
    t = sum_x + y
    compensation = t - sum_x - y
    sum_x = t

    if val == prev_value:
        num_consecutive_same_value += 1
    else:
        num_consecutive_same_value = 1
    prev_value = val

exit((nobs, sum_x, compensation, num_consecutive_same_value, prev_value))
