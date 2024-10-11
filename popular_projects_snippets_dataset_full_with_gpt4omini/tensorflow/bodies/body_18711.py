# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
init1 = init_ops_v2.Orthogonal(seed=1)
init2 = init_ops_v2.Orthogonal(seed=2)
self._identical_test(init1, init2, False, (10, 10))
