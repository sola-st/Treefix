# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
shape = (5, 6, 4, 2)
fan_in, _ = init_ops_v2._compute_fans(shape)
std = np.sqrt(1. / fan_in)
self._range_test(
    init_ops_v2.lecun_uniform(seed=123),
    shape,
    target_mean=0.,
    target_std=std)
