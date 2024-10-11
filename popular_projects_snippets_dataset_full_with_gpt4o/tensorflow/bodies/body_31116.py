# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
# [1, 2, 2, 1]
image = [[[[.1], [.2]], [[.3], [.4]]]]
# [2, 2, 1]
kernel = [[[.4], [.3]], [[.1], [.0]]]
# [1, 2, 2, 1]
out = [[[[.5], [.6]], [[.7], [.8]]]]
self._VerifyValues(
    image,
    kernel,
    strides=[1, 1],
    rates=[1, 1],
    padding="SAME",
    out=out,
    use_gpu=use_gpu,
    dtype=dtype)
