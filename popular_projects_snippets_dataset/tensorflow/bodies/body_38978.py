# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.force_cpu():
    # 1-D, values at index 0.
    sp_zero = sparse_tensor.SparseTensor([[0]], [0], [7])
    sp_one = sparse_tensor.SparseTensor([[0]], [1], [7])
    max_tf = sparse_ops.sparse_maximum(sp_zero, sp_one)
    min_tf = sparse_ops.sparse_minimum(sp_zero, sp_one)
    self._assertSparseTensorValueEqual(sp_one, max_tf)
    self._assertSparseTensorValueEqual(sp_zero, min_tf)

    # Values at different indices.
    sp_zero = sparse_tensor.SparseTensor([[0]], [0], [7])
    sp_zero_2 = sparse_tensor.SparseTensor([[1]], [0], [7])
    expected = sparse_tensor.SparseTensor([[0], [1]], [0, 0], [7])
    max_tf = sparse_ops.sparse_maximum(sp_zero, sp_zero_2)
    min_tf = sparse_ops.sparse_minimum(sp_zero, sp_zero_2)
    self._assertSparseTensorValueEqual(expected, max_tf)
    self._assertSparseTensorValueEqual(expected, min_tf)
