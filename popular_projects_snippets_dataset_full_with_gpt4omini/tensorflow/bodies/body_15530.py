# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape_test.py
"""Tests for the broadcast_dimension method.

    Verifies that:

    * `original.broadcast_dimension(axis, row_length) == broadcast`
    * `broadcast.broadcast_dimension(axis, row_length) == broadcast`
    * `broadcast.broadcast_dimension(axis, 1) == broadcast`

    Args:
      axis: The axis to broadcast
      row_length: The slice lengths to broadcast to.
      original_dim_sizes: The dimension sizes before broadcasting.
        original_dim_sizes[axis] should be equal to `1` or `row_length`.
      broadcast_dim_sizes: THe dimension sizes after broadcasting.
    """
original_shape = RaggedTensorDynamicShape.from_dim_sizes(original_dim_sizes)
bcast_shape = RaggedTensorDynamicShape.from_dim_sizes(broadcast_dim_sizes)
self.assertEqual(original_shape.rank, bcast_shape.rank)
# shape[axis].value == 1 and row_length > 1:
bcast1 = original_shape.broadcast_dimension(axis, row_length)
# shape[axis].value > 1 and row_length == shape[axis].value:
bcast2 = bcast_shape.broadcast_dimension(axis, row_length)
# shape[axis].value > 1 and row_length == 1:
bcast3 = bcast_shape.broadcast_dimension(axis, 1)

self.assertShapeEq(bcast1, bcast_shape)
self.assertShapeEq(bcast2, bcast_shape)
self.assertShapeEq(bcast3, bcast_shape)
