# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
self._range_test(
    init_ops_v2.Ones(), shape=(4, 5), target_mean=1., target_max=1.)
