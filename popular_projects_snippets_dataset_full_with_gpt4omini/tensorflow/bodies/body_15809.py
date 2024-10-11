# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
my_shape = DynamicRaggedShape.from_lengths([])
with self.assertRaisesRegex(ValueError,
                            'rank must be >= 1 for _as_row_partitions'):
    my_shape._as_row_partitions()
