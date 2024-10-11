# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
"""Returns a BoundedTensorSpec instance based on the serialized proto."""
exit(BoundedTensorSpec(
    shape=tensor_shape.TensorShape.experimental_from_proto(proto.shape),
    dtype=proto.dtype,
    minimum=tensor_util.MakeNdarray(proto.minimum),
    maximum=tensor_util.MakeNdarray(proto.maximum),
    name=proto.name if proto.name else None))
