# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_from_sparse_op_test.py
st1 = sparse_tensor.SparseTensor(indices=[[0]], values=[0], dense_shape=[3])
self.assertRaisesRegex(ValueError, r'rank\(st_input\) must be 2',
                       RaggedTensor.from_sparse, st1)

st2 = sparse_tensor.SparseTensor(
    indices=[[0, 0, 0]], values=[0], dense_shape=[3, 3, 3])
self.assertRaisesRegex(ValueError, r'rank\(st_input\) must be 2',
                       RaggedTensor.from_sparse, st2)

if not context.executing_eagerly():
    st3 = sparse_tensor.SparseTensor(
        indices=array_ops.placeholder(dtypes.int64),
        values=[0],
        dense_shape=array_ops.placeholder(dtypes.int64))
    self.assertRaisesRegex(ValueError, r'rank\(st_input\) must be 2',
                           RaggedTensor.from_sparse, st3)
