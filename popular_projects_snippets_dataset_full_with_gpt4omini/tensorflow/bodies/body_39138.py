# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
# All inputs must be 2D.
with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                            'Expected D2 of index to be 2'):
    st = sparse_tensor.SparseTensor([[0]], [0], [10])  # 1D SparseTensor
    self.evaluate(sparse_ops.sparse_cross([st]))

with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                            'Dense inputs should be a matrix'):
    dt = array_ops.zeros([0])  # 1D DenseTensor.
    self.evaluate(sparse_ops.sparse_cross([dt]))
