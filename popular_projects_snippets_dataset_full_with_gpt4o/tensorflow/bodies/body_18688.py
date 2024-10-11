# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
shape = (20, 6, 7)
self._range_test(
    init_ops_v2.RandomUniform(minval=-1, maxval=1, seed=124),
    shape,
    target_mean=0.,
    target_max=1,
    target_min=-1)
