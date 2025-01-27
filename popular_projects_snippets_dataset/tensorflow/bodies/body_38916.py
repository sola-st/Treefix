# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with ops.Graph().as_default():
    shape = constant_op.constant([2, 2], dtype=dtypes.int64)
    dynamic_shape = array_ops.placeholder_with_default(shape, shape=[2])
    ids = sparse_tensor.SparseTensor(
        indices=[[0, 0], [0, 1]],
        values=[1, 3],
        dense_shape=dynamic_shape)
    values = sparse_tensor.SparseTensor(
        indices=[[0, 0], [0, 1]],
        values=[0.4, 0.7],
        dense_shape=dynamic_shape)
    merged = sparse_ops.sparse_merge(
        sp_ids=ids, sp_values=values, vocab_size=5)
    self.assertEqual(5, merged.get_shape()[1])
