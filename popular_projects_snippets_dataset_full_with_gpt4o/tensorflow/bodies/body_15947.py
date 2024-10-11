# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Note that self_merge is only idempotent if no data is partially present.
with self.assertRaisesRegex(error_type, msg):
    dynamic_ragged_shape.DynamicRaggedShape.Spec(
        row_partitions=row_partitions,
        static_inner_shape=static_inner_shape,
        dtype=dtype)
