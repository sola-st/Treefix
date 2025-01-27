# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
self._range_test(
    init_ops_v2.Constant(2),
    shape=(5, 6, 4),
    target_mean=2,
    target_max=2,
    target_min=2)
