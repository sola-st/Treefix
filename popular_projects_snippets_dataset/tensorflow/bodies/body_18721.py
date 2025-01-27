# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
init = init_ops_v2.Identity()
shape = (10, 5)
with test_util.use_gpu():
    self.assertAllClose(self.evaluate(init(shape)), np.eye(*shape))
