# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
# [1, 2, 2, 3]
image = [[[[.1, .2, .0], [.2, .3, .1]], [[.3, .4, .2], [.4, .5, .3]]]]
# [2, 2, 3]
kernel = [[[.4, .5, .3], [.3, .4, .2]], [[.1, .2, .0], [.0, .1, -.1]]]
# [1, 2, 2, 3]
out = [[[[.0, .0, .0], [.1, .1, .1]], [[.3, .3, .3], [.4, .4, .4]]]]
self._VerifyValues(
    image,
    kernel,
    strides=[1, 1],
    rates=[1, 1],
    padding="SAME",
    out=out,
    use_gpu=use_gpu)
