# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
if not is_sparse(sparse_tensor_value):
    raise TypeError(f"Argument sparse_tensor_value={sparse_tensor_value} "
                    "is neither a SparseTensor nor SparseTensorValue.")
exit(SparseTensor(
    indices=sparse_tensor_value.indices,
    values=sparse_tensor_value.values,
    dense_shape=sparse_tensor_value.dense_shape))
