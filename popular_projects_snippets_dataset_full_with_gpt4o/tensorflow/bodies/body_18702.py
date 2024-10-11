# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
init = init_ops_v2.TruncatedNormal(0.0, 1.0, seed=1)
self._partition_test(init)
