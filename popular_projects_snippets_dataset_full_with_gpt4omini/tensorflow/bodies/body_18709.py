# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
self._range_test(
    init_ops_v2.Orthogonal(seed=123), shape=(20, 20), target_mean=0.)
