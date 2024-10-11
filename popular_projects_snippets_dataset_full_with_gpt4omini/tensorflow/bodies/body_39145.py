# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests mixed dense inputs."""
dense_inp_1 = constant_op.constant([[11, 333], [55555, 999999]],
                                   dtypes.int64)
dense_inp_2 = constant_op.constant([['batch1-FC2-F1', 'batch1-FC2-F2'],
                                    ['batch2-FC2-F1', 'batch2-FC2-F2']],
                                   dtypes.string)
inds, vals, shapes = gen_sparse_ops.sparse_cross_v2(
    indices=[],
    values=[],
    shapes=[],
    dense_inputs=[dense_inp_1, dense_inp_2],
    sep='_X_')
out = sparse_tensor.SparseTensor(inds, vals, shapes)
# pyformat: disable
expected_out = self._sparse_tensor([
    ['11_X_batch1-FC2-F1', '11_X_batch1-FC2-F2',
     '333_X_batch1-FC2-F1', '333_X_batch1-FC2-F2'
    ],
    ['55555_X_batch2-FC2-F1', '55555_X_batch2-FC2-F2',
     '999999_X_batch2-FC2-F1', '999999_X_batch2-FC2-F2'
    ]])
# pyformat: enable
with self.cached_session():
    self._assert_sparse_tensor_equals(expected_out, self.evaluate(out))
