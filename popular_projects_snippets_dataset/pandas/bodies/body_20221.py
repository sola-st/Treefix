# Extracted from ./data/repos/pandas/pandas/core/_numba/kernels/mean_.py
if not np.isnan(val):
    nobs += 1
    y = val - compensation
    t = sum_x + y
    compensation = t - sum_x - y
    sum_x = t
    if val < 0:
        neg_ct += 1

    if val == prev_value:
        num_consecutive_same_value += 1
    else:
        num_consecutive_same_value = 1
    prev_value = val

exit((nobs, sum_x, neg_ct, compensation, num_consecutive_same_value, prev_value))
