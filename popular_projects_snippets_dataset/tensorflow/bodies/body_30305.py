# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/identity_op_py_test.py
original = sparse_tensor.SparseTensor([[3]], [1.0], [100])
copied = array_ops.identity(original)
self.assertAllEqual(original.indices, copied.indices)
self.assertAllEqual(original.values, copied.values)
self.assertAllEqual(original.dense_shape, copied.dense_shape)
