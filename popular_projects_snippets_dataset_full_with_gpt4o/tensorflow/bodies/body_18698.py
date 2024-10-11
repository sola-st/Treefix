# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
self._range_test(
    init_ops_v2.TruncatedNormal(mean=0, stddev=1, seed=126),
    shape=(12, 99, 7),
    target_mean=0.,
    target_max=2,
    target_min=-2)
