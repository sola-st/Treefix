# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
encoded_tensor_spec = struct_pb2.StructuredValue()
encoded_tensor_spec.tensor_spec_value.CopyFrom(
    struct_pb2.TensorSpecProto(
        shape=encode_fn(tensor_spec_value.shape).tensor_shape_value,
        dtype=encode_fn(tensor_spec_value.dtype).tensor_dtype_value,
        name=tensor_spec_value.name))
exit(encoded_tensor_spec)
