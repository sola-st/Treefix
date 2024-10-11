# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
self.skipTest("Doesn't work without the graphs")
init1 = init_ops_v2.Orthogonal(seed=1)
init2 = init_ops_v2.Orthogonal(gain=3.14, seed=1)
with test_util.use_gpu():
    t1 = self.evaluate(init1(shape=(10, 10)))
    t2 = self.evaluate(init2(shape=(10, 10)))
self.assertAllClose(t1, t2 / 3.14)
