# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
init = init_ops_v2.RandomUniform(0, 7, seed=1)
self._partition_test(init)
