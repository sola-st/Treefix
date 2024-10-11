# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_fn_op_test.py
s = sparse_tensor.SparseTensor(
    indices=[[0, 0], [0, 1], [1, 0], [1, 1]],
    values=[0, 5, 0, 4],
    dense_shape=[2, 2],
)
t2 = ragged_tensor.RaggedTensor.from_sparse(s)
id_t2 = ragged_map_ops.map_fn(
    lambda x: x, t2,
)
self.assertAllEqual(id_t2, [[0, 5], [0, 4]])
