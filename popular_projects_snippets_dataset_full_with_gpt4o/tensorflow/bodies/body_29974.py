# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
with self.assertRaises(TypeError):
    constant_op.constant([1, 2, 3, 4, 5, 6, 7], shape=[10])
