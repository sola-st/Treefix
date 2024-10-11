# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
with test_util.use_gpu():
    init = init_ops_v2.constant_initializer(value)
    self.assertRaises(TypeError, init, shape=shape)
