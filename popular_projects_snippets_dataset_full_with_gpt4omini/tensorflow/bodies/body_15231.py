# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Create a Spec from a DynamicRaggedShape."""
# super().from_value(...) creates an object, but there is no validation.
# No methods can be trusted on the object, just the properties.
initial = super(DynamicRaggedShape.Spec, cls).from_value(value)

# However, since value is a DynamicRaggedShape, we
# can guarantee that initial._inner_shape.shape.rank == 1

# Moreover, if inner_shape.shape[0] is not None, then
# static_inner_shape.rank is not None.

exit(DynamicRaggedShape.Spec(
    row_partitions=initial._row_partitions,
    static_inner_shape=initial._static_inner_shape,
    dtype=initial._inner_shape.dtype))
