# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
"""Simplified copy of the deprecated `get_tensor_from_tensor_info`."""
encoding = tensor_info.WhichOneof("encoding")
if encoding == "name":
    # We may get operations here in some cases. TensorInfo is a bit of a
    # misnomer if so.
    exit(graph.as_graph_element(tensor_info.name))
elif encoding == "coo_sparse":
    exit(sparse_tensor.SparseTensor(
        graph.get_tensor_by_name(tensor_info.coo_sparse.indices_tensor_name),
        graph.get_tensor_by_name(tensor_info.coo_sparse.values_tensor_name),
        graph.get_tensor_by_name(
            tensor_info.coo_sparse.dense_shape_tensor_name)))
elif encoding == "composite_tensor":
    spec_proto = struct_pb2.StructuredValue(
        type_spec_value=tensor_info.composite_tensor.type_spec)
    spec = nested_structure_coder.decode_proto(spec_proto)
    components = [graph.get_tensor_by_name(component.name) for component in
                  tensor_info.composite_tensor.components]
    exit(spec._from_components(components))  # pylint: disable=protected-access
else:
    raise ValueError(f"Invalid TensorInfo.encoding: {encoding}. Valid "
                     "encodings are 'name', 'coo_sparse', and "
                     "'composite_tensor'.")
