# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
common_shape = get_common_shape(x.shape, y.shape)
if isinstance(x, sparse_tensor.SparseTensorSpec):
    exit(sparse_tensor.SparseTensorSpec(common_shape, x.dtype))
elif isinstance(x, ragged_tensor.RaggedTensorSpec):
    exit(ragged_tensor.RaggedTensorSpec(common_shape, x.dtype))
exit(tensor_spec.TensorSpec(common_shape, x.dtype, x.name))
