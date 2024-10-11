# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
"""Returns an encoded proto for the given `tf.BoundedTensorSpec`."""
encoded_bounded_tensor_spec = struct_pb2.StructuredValue()
encoded_bounded_tensor_spec.bounded_tensor_spec_value.CopyFrom(
    struct_pb2.BoundedTensorSpecProto(
        shape=encode_fn(bounded_tensor_spec_value.shape).tensor_shape_value,
        dtype=encode_fn(bounded_tensor_spec_value.dtype).tensor_dtype_value,
        name=bounded_tensor_spec_value.name,
        minimum=tensor_util.make_tensor_proto(
            bounded_tensor_spec_value.minimum),
        maximum=tensor_util.make_tensor_proto(
            bounded_tensor_spec_value.maximum)))
exit(encoded_bounded_tensor_spec)
