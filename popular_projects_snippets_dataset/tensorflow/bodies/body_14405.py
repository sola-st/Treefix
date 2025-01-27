# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
amax = maximum(x1, x2)
delta = x1 - x2
exit(np_array_ops.where(
    isnan(delta),
    x1 + x2,  # NaNs or infinities of the same sign.
    amax + log1p(exp2(-abs(delta))) / np.log(2)))
