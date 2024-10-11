# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
source = RaggedTensor.from_uniform_row_length([0, 1, 2, 3], 2)
target_shape = DynamicRaggedShape._from_inner_shape([1, 2, 2])
broadcaster = dynamic_ragged_shape._get_broadcaster(
    DynamicRaggedShape.from_tensor(source), target_shape)
flat_values = broadcaster.broadcast_flat_values(source)
self.assertAllEqual(flat_values, [[[0, 1], [2, 3]]])
