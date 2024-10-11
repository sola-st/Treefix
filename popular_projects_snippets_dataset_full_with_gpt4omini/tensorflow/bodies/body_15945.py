# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# The constructor detects if there is any additional information that
# can be inferred from what is given.
original = dynamic_ragged_shape.DynamicRaggedShape.Spec(
    row_partitions, static_inner_shape, inner_shape.dtype)
self.assertTensorShapeEqual(original._static_inner_shape,
                            static_inner_shape)
self.assertTensorSpecEqual(original._inner_shape, inner_shape)
for i, (a, b) in enumerate(zip(original._row_partitions, row_partitions)):
    self.assertRowPartitionSpecEqual(a, b, 'Error in partition ' + str(i))
