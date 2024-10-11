# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
row_partitions = row_partitions()
inner_shape = inner_shape()
with self.assertRaisesRegex(error_type, error_regex):
    DynamicRaggedShape(
        row_partitions, inner_shape, dtype=dtype, validate=validate)
