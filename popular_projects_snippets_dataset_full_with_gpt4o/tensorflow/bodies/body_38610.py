# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
self.assertEqual([],
                 array_ops.transpose(
                     constant_op.constant(1, dtype=dtypes.int32,
                                          shape=[])).get_shape().dims)
self.assertEqual([100],
                 array_ops.transpose(
                     constant_op.constant(
                         1, dtype=dtypes.int32,
                         shape=[100])).get_shape().dims)
self.assertEqual([37, 100],
                 array_ops.transpose(
                     constant_op.constant(
                         1, dtype=dtypes.int32,
                         shape=[100, 37])).get_shape().dims)
self.assertEqual([100, 37],
                 array_ops.transpose(
                     constant_op.constant(
                         1, dtype=dtypes.int32, shape=[100, 37]),
                     [0, 1]).get_shape().dims)
self.assertEqual([15, 37, 100],
                 array_ops.transpose(
                     constant_op.constant(
                         1, dtype=dtypes.int32,
                         shape=[100, 37, 15])).get_shape().dims)
self.assertEqual([15, 100, 37],
                 array_ops.transpose(
                     constant_op.constant(
                         1, dtype=dtypes.int32, shape=[100, 37, 15]),
                     [2, 0, 1]).get_shape().dims)
