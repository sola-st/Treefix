# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
init1 = init_ops_v2.RandomUniform(0, 7, seed=1)
init2 = init_ops_v2.RandomUniform(0, 7, seed=2)
self._identical_test(init1, init2, False)
