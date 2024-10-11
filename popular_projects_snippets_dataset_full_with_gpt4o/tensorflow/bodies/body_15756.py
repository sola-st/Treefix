# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(ValueError, msg):
    DynamicRaggedShape.from_lengths(
        lengths, num_row_partitions=num_row_partitions)
