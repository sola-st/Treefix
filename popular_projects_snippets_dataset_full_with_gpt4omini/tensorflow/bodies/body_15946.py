# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Note that self_merge is only idempotent if no data is partially present.
self.assertTensorShapeEqual(original._static_inner_shape,
                            expected_static_inner_shape)
self.assertTensorSpecEqual(original._inner_shape, expected_inner_shape)
for i, (a, b) in enumerate(
    zip(original._row_partitions, expected_row_partitions)):
    self.assertRowPartitionSpecEqual(a, b, 'Error in partition ' + str(i))
