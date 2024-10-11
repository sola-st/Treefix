# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
shape = (5, 6, 4, 2)
fan_in, fan_out = init_ops_v2._compute_fans(shape)
std = np.sqrt(2. / (fan_in + fan_out))
self._range_test(
    init_ops_v2.GlorotNormal(seed=123),
    shape,
    target_mean=0.,
    target_std=std)
