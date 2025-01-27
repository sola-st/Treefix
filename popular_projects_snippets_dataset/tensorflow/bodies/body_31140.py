# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
# [1, 3, 3, 1]
image = [[[[.1], [.2], [.3]], [[.4], [.5], [.6]], [[.7], [.8], [.9]]]]
# [2, 2, 1]
kernel = [[[.4], [.3]], [[.1], [.2]]]
# Because rate = 2.0, the effective kernel is [3, 3, 1]:
# kernel_eff = [[[.4], [.0], [.3]],
#               [[.0], [.0], [.0]],
#               [[.1], [.0], [.2]]]
# [1, 3, 3, 1]
out = [[[[.1], [.1], [.2]], [[0.1], [-.1], [.0]], [[.4], [.2], [.3]]]]
self._VerifyValues(
    image,
    kernel,
    strides=[1, 1],
    rates=[2, 2],
    padding="SAME",
    out=out,
    use_gpu=use_gpu)
