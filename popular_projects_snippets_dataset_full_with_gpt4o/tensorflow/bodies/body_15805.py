# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
rps = _to_row_partitions_from_lengths(rps)
actual = DynamicRaggedShape.from_row_partitions(rps)
expected = DynamicRaggedShape.from_lengths(
    lengths_e)._with_num_row_partitions(num_row_partitions_e)
self.assertShapeEq(expected, actual)
