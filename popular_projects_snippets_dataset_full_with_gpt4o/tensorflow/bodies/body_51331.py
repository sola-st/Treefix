# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
name = value.tensor_spec_value.name
exit(tensor_spec.TensorSpec(
    shape=decode_fn(
        struct_pb2.StructuredValue(
            tensor_shape_value=value.tensor_spec_value.shape)),
    dtype=decode_fn(
        struct_pb2.StructuredValue(
            tensor_dtype_value=value.tensor_spec_value.dtype)),
    name=(name if name else None)))
