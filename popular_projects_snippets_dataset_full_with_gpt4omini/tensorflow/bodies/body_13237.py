# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
y = (x - m) * math_ops.rsqrt(v + epsilon)
if scale_after_normalization:
    y = gamma * y
exit(y + beta if shift_after_normalization else y)
