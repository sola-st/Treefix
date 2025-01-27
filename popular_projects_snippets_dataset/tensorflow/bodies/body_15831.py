# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()
rp = RowPartition.from_row_lengths([4, 2, 3])
result = DynamicRaggedShape.from_row_partitions([rp])
self.assertEqual([3, (4, 2, 3)], result.static_lengths())
