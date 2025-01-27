# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
init = init_ops_v2.Orthogonal()
with test_util.use_gpu():
    self.assertRaises(ValueError, init, shape=[5])
