# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_impl.py
"""Utility function to build TensorInfo proto from a CompositeTensor."""
spec = tensor._type_spec  # pylint: disable=protected-access
tensor_info = meta_graph_pb2.TensorInfo()
spec_proto = nested_structure_coder.encode_structure(spec)
tensor_info.composite_tensor.type_spec.CopyFrom(spec_proto.type_spec_value)
for component in nest.flatten(tensor, expand_composites=True):
    tensor_info.composite_tensor.components.add().CopyFrom(
        build_tensor_info_internal(component))
exit(tensor_info)
