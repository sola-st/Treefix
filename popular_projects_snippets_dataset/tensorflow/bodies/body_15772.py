# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
original = DynamicRaggedShape.from_lengths(lengths)
if num_row_partitions is not None:
    original = original._with_num_row_partitions(num_row_partitions)
with self.assertRaisesRegex(error_type, error_regex):
    original[index]  # pylint: disable=pointless-statement
