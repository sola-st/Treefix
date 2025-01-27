# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests with large batch size to force multithreading."""
batch_size = 5000
col1 = []
col2 = []
col3 = []
for b in range(batch_size):
    col1.append(
        ['batch%d-FC1-F1' % b,
         'batch%d-FC1-F2' % b,
         'batch%d-FC1-F3' % b])
    col2.append(['batch%d-FC2-F1' % b])
    col3.append(['batch%d-FC3-F1' % b, 'batch%d-FC3-F2' % b])
sp_inp_1 = self._sparse_tensor(col1)
sp_inp_2 = self._sparse_tensor(col2)
sp_inp_3 = self._sparse_tensor(col3)

inds, vals, shapes = gen_sparse_ops.sparse_cross_v2(
    indices=[sp_inp_1.indices, sp_inp_2.indices, sp_inp_3.indices],
    values=[sp_inp_1.values, sp_inp_2.values, sp_inp_3.values],
    shapes=[
        sp_inp_1.dense_shape, sp_inp_2.dense_shape, sp_inp_3.dense_shape
    ],
    dense_inputs=[],
    sep='_X_')

col_out = []
for b in range(batch_size):
    col_out.append([
        'batch%d-FC1-F1_X_batch%d-FC2-F1_X_batch%d-FC3-F1' % (b, b, b),
        'batch%d-FC1-F1_X_batch%d-FC2-F1_X_batch%d-FC3-F2' % (b, b, b),
        'batch%d-FC1-F2_X_batch%d-FC2-F1_X_batch%d-FC3-F1' % (b, b, b),
        'batch%d-FC1-F2_X_batch%d-FC2-F1_X_batch%d-FC3-F2' % (b, b, b),
        'batch%d-FC1-F3_X_batch%d-FC2-F1_X_batch%d-FC3-F1' % (b, b, b),
        'batch%d-FC1-F3_X_batch%d-FC2-F1_X_batch%d-FC3-F2' % (b, b, b)
    ])

expected_out = self._sparse_tensor(col_out)
out = sparse_tensor.SparseTensor(inds, vals, shapes)
with self.cached_session():
    self._assert_sparse_tensor_equals(expected_out, self.evaluate(out))
