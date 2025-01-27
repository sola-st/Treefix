# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
init1 = init_ops.convolutional_orthogonal_3d()
with self.session(graph=ops.Graph(), use_gpu=True):
    self.assertRaises(ValueError, init1, shape=[3, 3, 3, 6, 5])
