# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
m = np.max(logx, axis=axis, keepdims=True)
sum_ = np.sum(w * np.exp(logx - m), axis=axis, keepdims=keep_dims)
sgn = np.sign(sum_)
if not keep_dims:
    m = np.squeeze(m, axis=axis)
exit((m + np.log(sgn * sum_), sgn))
