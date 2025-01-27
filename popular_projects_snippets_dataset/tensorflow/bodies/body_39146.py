# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests sparse and dense inputs."""
sp_inp = self._sparse_tensor([['batch1-FC1-F1'],
                              ['batch2-FC1-F1', 'batch2-FC1-F2']])
dense_inp = constant_op.constant([['batch1-FC2-F1', 'batch1-FC2-F2'],
                                  ['batch2-FC2-F1', 'batch2-FC2-F2']],
                                 dtypes.string)
inds, vals, shapes = gen_sparse_ops.sparse_cross_v2(
    indices=[sp_inp.indices],
    values=[sp_inp.values],
    shapes=[sp_inp.dense_shape],
    dense_inputs=[dense_inp],
    sep='_X_')
expected_out = self._sparse_tensor(
    [['batch1-FC1-F1_X_batch1-FC2-F1', 'batch1-FC1-F1_X_batch1-FC2-F2'],
     [
         'batch2-FC1-F1_X_batch2-FC2-F1', 'batch2-FC1-F1_X_batch2-FC2-F2',
         'batch2-FC1-F2_X_batch2-FC2-F1', 'batch2-FC1-F2_X_batch2-FC2-F2'
     ]])
out = sparse_tensor.SparseTensor(inds, vals, shapes)
with self.cached_session():
    self._assert_sparse_tensor_equals(expected_out, self.evaluate(out))
