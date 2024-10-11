# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
sp_inp_1 = self._sparse_tensor(
    [['batch1-FC1-F1', 'batch1-FC1-F2', 'batch1-FC1-F3']])
sp_inp_2 = self._sparse_tensor([['batch1-FC2-F1']])
sp_inp_3 = self._sparse_tensor([['batch1-FC3-F1', 'batch1-FC3-F2']])
inds, vals, shapes = gen_sparse_ops.sparse_cross_hashed(
    indices=[sp_inp_1.indices, sp_inp_2.indices, sp_inp_3.indices],
    values=[sp_inp_1.values, sp_inp_2.values, sp_inp_3.values],
    shapes=[
        sp_inp_1.dense_shape, sp_inp_2.dense_shape, sp_inp_3.dense_shape
    ],
    dense_inputs=[],
    strong_hash=False,
    num_buckets=1000,
    salt=[137, 173])
output = sparse_tensor.SparseTensor(inds, vals, shapes)
inds_2, vals_2, shapes_2 = gen_sparse_ops.sparse_cross_hashed(
    indices=[sp_inp_1.indices, sp_inp_2.indices, sp_inp_3.indices],
    values=[sp_inp_1.values, sp_inp_2.values, sp_inp_3.values],
    shapes=[
        sp_inp_1.dense_shape, sp_inp_2.dense_shape, sp_inp_3.dense_shape
    ],
    dense_inputs=[],
    strong_hash=True,
    num_buckets=1000,
    salt=[137, 1])
output_2 = sparse_tensor.SparseTensor(inds_2, vals_2, shapes_2)
with self.cached_session():
    out = self.evaluate(output)
    out_2 = self.evaluate(output_2)
    self.assertAllEqual(out.indices, out_2.indices)
    self.assertNotAllEqual(out.values, out_2.values)
