# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(ValueError, 'row_partitions cannot be empty'):
    DynamicRaggedShape.from_row_partitions([])
