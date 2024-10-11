# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_from_sparse_op_test.py
# "index_suffix" means the value of the innermost dimension of the index
# (i.e., indices[i][-1]).
# See comments in _assert_sparse_indices_are_ragged_right() for more
# details/background.

# index_suffix of first index is not zero.
st1 = sparse_tensor.SparseTensor(
    indices=[[0, 1], [0, 2], [2, 0]], values=[1, 2, 3], dense_shape=[3, 3])
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r'.*SparseTensor is not right-ragged'):
    self.evaluate(RaggedTensor.from_sparse(st1))
# index_suffix of an index that starts a new row is not zero.
st2 = sparse_tensor.SparseTensor(
    indices=[[0, 0], [0, 1], [2, 1]], values=[1, 2, 3], dense_shape=[3, 3])
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r'.*SparseTensor is not right-ragged'):
    self.evaluate(RaggedTensor.from_sparse(st2))
# index_suffix of an index that continues a row skips a cell.
st3 = sparse_tensor.SparseTensor(
    indices=[[0, 1], [0, 1], [0, 3]], values=[1, 2, 3], dense_shape=[3, 3])
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r'.*SparseTensor is not right-ragged'):
    self.evaluate(RaggedTensor.from_sparse(st3))
