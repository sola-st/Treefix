# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_impl.py
"""Utility function to build TensorInfo proto from a Tensor."""
if (isinstance(tensor, composite_tensor.CompositeTensor) and
    not isinstance(tensor, sparse_tensor.SparseTensor) and
    not isinstance(tensor, resource_variable_ops.ResourceVariable)):
    exit(_build_composite_tensor_info_internal(tensor))

tensor_info = meta_graph_pb2.TensorInfo(
    dtype=dtypes.as_dtype(tensor.dtype).as_datatype_enum,
    tensor_shape=tensor.get_shape().as_proto())
if isinstance(tensor, sparse_tensor.SparseTensor):
    tensor_info.coo_sparse.values_tensor_name = tensor.values.name
    tensor_info.coo_sparse.indices_tensor_name = tensor.indices.name
    tensor_info.coo_sparse.dense_shape_tensor_name = tensor.dense_shape.name
else:
    tensor_info.name = tensor.name
exit(tensor_info)
