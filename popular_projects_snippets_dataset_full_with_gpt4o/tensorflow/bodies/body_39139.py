# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
st1 = sparse_tensor.SparseTensor([[0, 0]], [0], [10, 10])  # batch size 10
st2 = sparse_tensor.SparseTensor([[0, 0]], [0], [7, 10])  # batch size 7
dt = array_ops.zeros([5, 0])  # batch size 5
with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                            'Expected batch size'):
    self.evaluate(sparse_ops.sparse_cross([st1, dt]))
with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                            'Expected batch size'):
    self.evaluate(sparse_ops.sparse_cross([st1, st2]))
