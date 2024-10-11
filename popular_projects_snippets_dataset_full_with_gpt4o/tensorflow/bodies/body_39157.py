# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests 3x1x2 permutation with hashed output."""
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
    num_buckets=1000,
    salt=[137, 173],
    strong_hash=False)
output = sparse_tensor.SparseTensor(inds, vals, shapes)
with self.cached_session():
    out = self.evaluate(output)
    self.assertEqual(6, len(out.values))
    self.assertAllEqual([[0, i] for i in range(6)], out.indices)
    self.assertTrue(all(x < 1000 and x >= 0 for x in out.values))
    all_values_are_different = len(out.values) == len(set(out.values))
    self.assertTrue(all_values_are_different)
