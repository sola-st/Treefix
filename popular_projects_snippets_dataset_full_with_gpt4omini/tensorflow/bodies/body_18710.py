# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
self.skipTest("Doesn't work without the graphs")
init1 = init_ops_v2.Orthogonal(seed=1)
init2 = init_ops_v2.Orthogonal(seed=1)
self._identical_test(init1, init2, True, (10, 10))
