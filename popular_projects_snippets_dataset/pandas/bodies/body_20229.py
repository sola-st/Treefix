# Extracted from ./data/repos/pandas/pandas/core/_numba/kernels/sum_.py
if not np.isnan(val):
    nobs -= 1
    y = -val - compensation
    t = sum_x + y
    compensation = t - sum_x - y
    sum_x = t
exit((nobs, sum_x, compensation))
