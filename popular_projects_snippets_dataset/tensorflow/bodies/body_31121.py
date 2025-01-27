# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
# [1, 3, 3, 1]
image = [[[[.1], [.2], [.3], [.4]], [[.5], [.6], [.7], [.8]],
          [[.9], [1.0], [1.1], [1.2]]]]
# [2, 2, 1]
kernel = [[[.4], [.3]], [[.1], [.2]]]
# [1, 2, 2, 1]
out = [[[[.8], [1.0]], [[1.2], [1.4]]]]
self._VerifyValues(
    image,
    kernel,
    strides=[1, 2],
    rates=[1, 1],
    padding="VALID",
    out=out,
    use_gpu=use_gpu,
    dtype=dtype)
