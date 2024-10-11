# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
source = DynamicRaggedShape.from_lengths(source_lengths)
if source_num_row_partitions is not None:
    source = source._with_num_row_partitions(source_num_row_partitions)
target = DynamicRaggedShape.from_lengths(target_lengths)
if target_num_row_partitions is not None:
    target = target._with_num_row_partitions(target_num_row_partitions)

expected_gather_indices = [
    _LayerBroadcaster.from_gather_index(x) for x in expected_gather_indices
]
actual = dynamic_ragged_shape._get_broadcaster(source, target)
expected = dynamic_ragged_shape._Broadcaster(source, target,
                                             expected_gather_indices)
self.assertBroadcasterEq(actual, expected)
