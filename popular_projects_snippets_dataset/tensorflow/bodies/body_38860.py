# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_slice_op_test.py
sp_input = self._SparseTensor_4x6()
start, size = [0, 0], [4, 1]
sp_output = sparse_ops.sparse_slice(sp_input, start, size)
input_grad_vals = sparse_ops.sparse_slice_grad(sp_output.values,
                                               sp_input.indices, start,
                                               sp_output.indices)
# pyformat: disable
self.assertAllEqual(input_grad_vals, [0, 0, 0, 0,
                                      0, 0, 0,
                                      20, 0, 0,
                                      30, 0, 0, 0])
# pyformat: enable

start, size = [0, 1], [4, 1]
sp_output = sparse_ops.sparse_slice(sp_input, start, size)
input_grad_vals = sparse_ops.sparse_slice_grad(sp_output.values,
                                               sp_input.indices, start,
                                               sp_output.indices)
# pyformat: disable
self.assertAllEqual(input_grad_vals, [0, 0, 0, 0,
                                      11, 0, 0,
                                      0, 0, 0,
                                      0, 0, 0, 0])
# pyformat: enable

start, size = [1, 3], [3, 1]
sp_output = sparse_ops.sparse_slice(sp_input, start, size)
input_grad_vals = sparse_ops.sparse_slice_grad(sp_output.values,
                                               sp_input.indices, start,
                                               sp_output.indices)
# pyformat: disable
self.assertAllEqual(input_grad_vals, [0, 0, 0, 0,
                                      0, 13, 0,
                                      0, 23, 0,
                                      0, 0, 33, 0])
# pyformat: enable

# Test empty slice of non-empty input.
start, size = [2, 1], [2, 1]
sp_output = sparse_ops.sparse_slice(sp_input, start, size)
input_grad_vals = sparse_ops.sparse_slice_grad(sp_output.values,
                                               sp_input.indices, start,
                                               sp_output.indices)
# pyformat: disable
self.assertAllEqual(input_grad_vals, [0, 0, 0, 0,
                                      0, 0, 0,
                                      0, 0, 0,
                                      0, 0, 0, 0])
# pyformat: enable

sp_input = self._SparseTensor_4x6_empty()
start, size = [0, 0], [4, 1]
sp_output = sparse_ops.sparse_slice(sp_input, start, size)
input_grad_vals = sparse_ops.sparse_slice_grad(sp_output.values,
                                               sp_input.indices, start,
                                               sp_output.indices)
self.assertAllEqual(input_grad_vals, [])
