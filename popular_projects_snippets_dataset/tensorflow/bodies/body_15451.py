# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_from_sparse_op_test.py
if not context.executing_eagerly():
    st1 = sparse_tensor.SparseTensor(
        indices=[[0, 0]],
        values=[0],
        dense_shape=array_ops.placeholder(dtypes.int64))
    st2 = sparse_tensor.SparseTensor(
        indices=array_ops.placeholder(dtypes.int64),
        values=[0],
        dense_shape=[4, 3])

    # Shouldn't throw ValueError
    RaggedTensor.from_sparse(st1)
    RaggedTensor.from_sparse(st2)
