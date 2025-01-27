# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests when one column is empty.

    The crossed tensor should be empty.
    """
sp_inp_1 = self._sparse_tensor([['batch1-FC1-F1', 'batch1-FC1-F2']])
sp_inp_2 = self._sparse_tensor([], 1)
sp_inp_3 = self._sparse_tensor([['batch1-FC3-F1', 'batch1-FC3-F2']])
inds, vals, shapes = gen_sparse_ops.sparse_cross_v2(
    indices=[sp_inp_1.indices, sp_inp_2.indices, sp_inp_3.indices],
    values=[sp_inp_1.values, sp_inp_2.values, sp_inp_3.values],
    shapes=[
        sp_inp_1.dense_shape, sp_inp_2.dense_shape, sp_inp_3.dense_shape
    ],
    dense_inputs=[],
    sep='_X_')
out = sparse_tensor.SparseTensor(inds, vals, shapes)
with self.cached_session():
    self._assert_sparse_tensor_empty(self.evaluate(out))
