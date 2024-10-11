# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
source_shape = DynamicRaggedShape(
    [RowPartition.from_row_splits(constant_op.constant([0, 1, 2]))],
    constant_op.constant([3]))
target_shape = DynamicRaggedShape(
    [RowPartition.from_row_splits(constant_op.constant([0, 1, 2]))],
    constant_op.constant([3]))
layer_broadcasters = [
    _LayerBroadcaster.from_gather_index(constant_op.constant([0, 1, 2])),
    _LayerBroadcaster.from_gather_index(constant_op.constant([0, 1, 2]))
]
bc = dynamic_ragged_shape._Broadcaster(source_shape, target_shape,
                                       layer_broadcasters)
actual = str(bc)
self.assertRegex(actual, '.src_shape..DynamicRaggedShape')
