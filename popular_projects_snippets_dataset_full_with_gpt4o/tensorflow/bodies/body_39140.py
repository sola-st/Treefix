# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests a simple scenario."""
sp_inp_1 = self._sparse_tensor([['batch1-FC1-F1'],
                                ['batch2-FC1-F1', 'batch2-FC1-F2']])
sp_inp_2 = self._sparse_tensor([['batch1-FC2-F1'],
                                ['batch2-FC2-F1', 'batch2-FC2-F2']])
inds, vals, shapes = gen_sparse_ops.sparse_cross_v2(
    indices=[sp_inp_1.indices, sp_inp_2.indices],
    values=[sp_inp_1.values, sp_inp_2.values],
    shapes=[sp_inp_1.dense_shape, sp_inp_2.dense_shape],
    dense_inputs=[],
    sep='_X_')
out = sparse_tensor.SparseTensor(inds, vals, shapes)
# pyformat: disable
expected_out = self._sparse_tensor([
    ['batch1-FC1-F1_X_batch1-FC2-F1'],
    ['batch2-FC1-F1_X_batch2-FC2-F1',
     'batch2-FC1-F1_X_batch2-FC2-F2',
     'batch2-FC1-F2_X_batch2-FC2-F1',
     'batch2-FC1-F2_X_batch2-FC2-F2'
    ]])
# pyformat: enable
with self.cached_session():
    self._assert_sparse_tensor_equals(expected_out, self.evaluate(out))
