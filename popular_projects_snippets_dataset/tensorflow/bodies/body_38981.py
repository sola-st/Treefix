# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.force_cpu():
    sp_zero = sparse_tensor.SparseTensor([[0, 0]], [0], [1, 1])
    sp_one = sparse_tensor.SparseTensor([[0]], [1], [2])
    with self.assertRaisesOpError("Operands do not have the same ranks"):
        self.evaluate(sparse_ops.sparse_maximum(sp_zero, sp_one))

    sp_zero = sparse_tensor.SparseTensor([[0]], [0], [1])
    sp_one = sparse_tensor.SparseTensor([[0]], [1], [2])
    with self.assertRaisesOpError("Operands' shapes do not match"):
        self.evaluate(sparse_ops.sparse_maximum(sp_zero, sp_one))
