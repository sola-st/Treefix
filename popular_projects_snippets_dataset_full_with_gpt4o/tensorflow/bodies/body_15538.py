# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_where_op.py
"""Ragged version of tf.where_v2(condition, x, y)."""
# Broadcast x, y, and condition to have the same shape.
if not (condition.shape.is_fully_defined() and x.shape.is_fully_defined() and
        y.shape.is_fully_defined() and x.shape == y.shape and
        condition.shape == x.shape):
    shape_c = ragged_tensor_shape.RaggedTensorDynamicShape.from_tensor(
        condition)
    shape_x = ragged_tensor_shape.RaggedTensorDynamicShape.from_tensor(x)
    shape_y = ragged_tensor_shape.RaggedTensorDynamicShape.from_tensor(y)
    shape = ragged_tensor_shape.broadcast_dynamic_shape(
        shape_c, ragged_tensor_shape.broadcast_dynamic_shape(shape_x, shape_y))
    condition = ragged_tensor_shape.broadcast_to(condition, shape)
    x = ragged_tensor_shape.broadcast_to(x, shape)
    y = ragged_tensor_shape.broadcast_to(y, shape)

condition_is_ragged = isinstance(condition, ragged_tensor.RaggedTensor)
x_is_ragged = isinstance(x, ragged_tensor.RaggedTensor)
y_is_ragged = isinstance(y, ragged_tensor.RaggedTensor)
if not (condition_is_ragged or x_is_ragged or y_is_ragged):
    exit(array_ops.where_v2(condition, x, y))

exit(ragged_functional_ops.map_flat_values(array_ops.where_v2, condition, x,
                                             y))
