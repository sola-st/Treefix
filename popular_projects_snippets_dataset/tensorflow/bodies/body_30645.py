# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
init = init_ops.identity_initializer()
with self.session(graph=ops.Graph(), use_gpu=True):
    self.assertRaises(ValueError, init, shape=[5, 7, 7])
    self.assertRaises(ValueError, init, shape=[5])
    self.assertRaises(ValueError, init, shape=[])
