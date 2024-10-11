# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
self.assertTensorShapeEqual(a._static_inner_shape, b._static_inner_shape)
self.assertTensorSpecEqual(a._inner_shape, b._inner_shape)
for i, (a, b) in enumerate(zip(a._row_partitions, b._row_partitions)):
    self.assertRowPartitionSpecEqual(a, b, 'Error in partition ' + str(i))
