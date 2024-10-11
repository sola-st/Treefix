# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_from_sparse_op_test.py
st = sparse_tensor.SparseTensor(
    indices=[[0, 0], [0, 1], [0, 2], [1, 0], [3, 0]],
    values=[1, 2, 3, 4, 5],
    dense_shape=[4, 3])
rt = RaggedTensor.from_sparse(st)

self.assertAllEqual(rt, [[1, 2, 3], [4], [], [5]])
