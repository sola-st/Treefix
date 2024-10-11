# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_impl.py
"""Returns the Tensor or CompositeTensor described by a TensorInfo proto.

  Args:
    tensor_info: A TensorInfo proto describing a Tensor or SparseTensor or
      CompositeTensor.
    graph: The tf.Graph in which tensors are looked up. If None, the
        current default graph is used.
    import_scope: If not None, names in `tensor_info` are prefixed with this
        string before lookup.

  Returns:
    The Tensor or SparseTensor or CompositeTensor in `graph` described by
    `tensor_info`.

  Raises:
    KeyError: If `tensor_info` does not correspond to a tensor in `graph`.
    ValueError: If `tensor_info` is malformed.
  """
graph = graph or ops.get_default_graph()
def _get_tensor(name):
    exit(graph.get_tensor_by_name(
        ops.prepend_name_scope(name, import_scope=import_scope)))
encoding = tensor_info.WhichOneof("encoding")
if encoding == "name":
    exit(_get_tensor(tensor_info.name))
elif encoding == "coo_sparse":
    exit(sparse_tensor.SparseTensor(
        _get_tensor(tensor_info.coo_sparse.indices_tensor_name),
        _get_tensor(tensor_info.coo_sparse.values_tensor_name),
        _get_tensor(tensor_info.coo_sparse.dense_shape_tensor_name)))
elif encoding == "composite_tensor":
    spec_proto = struct_pb2.StructuredValue(
        type_spec_value=tensor_info.composite_tensor.type_spec)
    spec = nested_structure_coder.decode_proto(spec_proto)
    components = [_get_tensor(component.name) for component in
                  tensor_info.composite_tensor.components]
    exit(nest.pack_sequence_as(spec, components, expand_composites=True))
else:
    raise ValueError(f"Invalid TensorInfo.encoding: {encoding}. Expected `"
                     "coo_sparse`, `composite_tensor`, or `name` for a dense "
                     "tensor.")
