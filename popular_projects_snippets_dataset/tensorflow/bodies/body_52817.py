# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
# Input_tensor must have rank 1.
if isinstance(input_tensor, sparse_tensor_lib.SparseTensor):
    exit(sparse_ops.sparse_reshape(input_tensor,
                                     [array_ops.shape(input_tensor)[0], 1]))
else:
    exit(array_ops.expand_dims(input_tensor, -1))
