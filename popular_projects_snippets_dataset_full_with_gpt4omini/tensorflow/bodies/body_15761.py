# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
origin_shape = DynamicRaggedShape([], inner_shape=[])
dest_shape = DynamicRaggedShape([RowPartition.from_row_splits([0, 2, 3])],
                                inner_shape=[3])
actual = dynamic_ragged_shape._get_broadcaster(origin_shape, dest_shape)
expected = dynamic_ragged_shape._Broadcaster(origin_shape, dest_shape, [])
self.assertBroadcasterEq(actual, expected)
