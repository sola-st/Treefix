# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
sp_inp_1 = self._sparse_tensor([['batch1-FC1-F1']])
sp_inp_2 = self._sparse_tensor([['batch1-FC2-F1']])
sp_inp_3 = self._sparse_tensor([['batch1-FC3-F1']])
inds, vals, shapes = gen_sparse_ops.sparse_cross_hashed(
    indices=[sp_inp_1.indices, sp_inp_2.indices, sp_inp_3.indices],
    values=[sp_inp_1.values, sp_inp_2.values, sp_inp_3.values],
    shapes=[
        sp_inp_1.dense_shape, sp_inp_2.dense_shape, sp_inp_3.dense_shape
    ],
    dense_inputs=[],
    num_buckets=0,
    salt=[1, 1],
    strong_hash=False)
# Check actual hashed output to prevent unintentional hashing changes.
expected_out = self._sparse_tensor([[9186962005966787372]])
out = sparse_tensor.SparseTensor(inds, vals, shapes)
with self.cached_session():
    self._assert_sparse_tensor_equals(expected_out, self.evaluate(out))

# salt is not being used when `strong_hash` is False.
inds_2, vals_2, shapes_2 = gen_sparse_ops.sparse_cross_hashed(
    indices=[sp_inp_1.indices, sp_inp_2.indices, sp_inp_3.indices],
    values=[sp_inp_1.values, sp_inp_2.values, sp_inp_3.values],
    shapes=[
        sp_inp_1.dense_shape, sp_inp_2.dense_shape, sp_inp_3.dense_shape
    ],
    dense_inputs=[],
    num_buckets=0,
    salt=[137, 173],
    strong_hash=False)
out_2 = sparse_tensor.SparseTensor(inds_2, vals_2, shapes_2)
with self.cached_session():
    self._assert_sparse_tensor_equals(expected_out, self.evaluate(out_2))
