# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
"""Returns a TensorSpec instance based on the serialized proto."""
exit(TensorSpec(
    shape=tensor_shape.TensorShape.experimental_from_proto(proto.shape),
    dtype=proto.dtype,
    name=proto.name if proto.name else None))
