# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_from_sparse_op_test.py
st = sparse_tensor.SparseTensor(
    indices=array_ops.zeros([0, 2], dtype=dtypes.int64),
    values=[],
    dense_shape=[4, 3])
rt = RaggedTensor.from_sparse(st)

self.assertAllEqual(rt, [[], [], [], []])
