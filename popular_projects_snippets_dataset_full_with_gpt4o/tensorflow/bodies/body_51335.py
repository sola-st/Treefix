# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
btsv = value.bounded_tensor_spec_value
name = btsv.name
exit(tensor_spec.BoundedTensorSpec(
    shape=decode_fn(
        struct_pb2.StructuredValue(tensor_shape_value=btsv.shape)),
    dtype=decode_fn(
        struct_pb2.StructuredValue(tensor_dtype_value=btsv.dtype)),
    minimum=tensor_util.MakeNdarray(btsv.minimum),
    maximum=tensor_util.MakeNdarray(btsv.maximum),
    name=(name if name else None)))
