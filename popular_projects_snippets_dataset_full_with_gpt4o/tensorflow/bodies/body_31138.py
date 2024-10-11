# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
# [2, 2, 2, 1]
image = [[[[.1], [.2]], [[.3], [.4]]], [[[.2], [.3]], [[.4], [.5]]]]
# [2, 2, 1]
kernel = [[[.4], [.3]], [[.1], [.0]]]
# [2, 2, 2, 1]
out = [[[[.0], [.1]], [[.3], [.4]]], [[[.1], [.2]], [[.4], [.5]]]]
self._VerifyValues(
    image,
    kernel,
    strides=[1, 1],
    rates=[1, 1],
    padding="SAME",
    out=out,
    use_gpu=use_gpu)
