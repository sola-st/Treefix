# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
"""Static check that shapes are compatible."""
# Broadcast shape also checks that u and v are compatible.
uv_shape = array_ops.broadcast_static_shape(
    self.u.shape, self.v.shape)

batch_shape = array_ops.broadcast_static_shape(
    self.base_operator.batch_shape, uv_shape[:-2])

tensor_shape.Dimension(
    self.base_operator.domain_dimension).assert_is_compatible_with(
        uv_shape[-2])

if self._diag_update is not None:
    tensor_shape.dimension_at_index(uv_shape, -1).assert_is_compatible_with(
        self._diag_update.shape[-1])
    array_ops.broadcast_static_shape(
        batch_shape, self._diag_update.shape[:-1])
