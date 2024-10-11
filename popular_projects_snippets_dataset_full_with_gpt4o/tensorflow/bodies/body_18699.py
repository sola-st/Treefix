# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
self.skipTest("Not seeming to work in Eager mode")
init1 = init_ops_v2.TruncatedNormal(0.0, 1.0, seed=1)
init2 = init_ops_v2.TruncatedNormal(0.0, 1.0, seed=1)
self._identical_test(init1, init2, True)
