# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
self._range_test(
    init_ops_v2.RandomNormal(mean=0, stddev=1, seed=153),
    shape=(8, 12, 99),
    target_mean=0.,
    target_std=1)
