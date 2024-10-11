# Extracted from ./data/repos/pandas/pandas/core/_numba/kernels/var_.py
if not np.isnan(val):
    nobs -= 1
    if nobs:
        prev_mean = mean_x - compensation
        y = val - compensation
        t = y - mean_x
        compensation = t + mean_x - y
        delta = t
        mean_x -= delta / nobs
        ssqdm_x -= (val - prev_mean) * (val - mean_x)
    else:
        mean_x = 0
        ssqdm_x = 0
exit((nobs, mean_x, ssqdm_x, compensation))
