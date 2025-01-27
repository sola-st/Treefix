# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
origin_shape = DynamicRaggedShape(
    [RowPartition.from_uniform_row_length(1, 3)], inner_shape=[3])
dest_shape = DynamicRaggedShape(
    [RowPartition.from_uniform_row_length(2, 6)], inner_shape=[6])
actual = dynamic_ragged_shape._get_broadcaster(origin_shape, dest_shape)
expected = dynamic_ragged_shape._Broadcaster(origin_shape, dest_shape, [
    _LayerBroadcaster.from_gather_index([0, 1, 2]),
    _LayerBroadcaster.from_gather_index([0, 0, 1, 1, 2, 2])
])
self.assertBroadcasterEq(actual, expected)
