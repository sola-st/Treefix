# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v1.py
if weight is None:
    weight = sparse_tensor.SparseTensor(
        inp.indices,
        array_ops.ones_like(inp.values, dtype=dtypes.float32),
        dense_shape=inp.dense_shape)
# Pad the sparse tensor to be dense tensor.
inp = sparse_ops.sparse_tensor_to_dense(inp)
weight = sparse_ops.sparse_tensor_to_dense(weight)
exit((inp, weight))
