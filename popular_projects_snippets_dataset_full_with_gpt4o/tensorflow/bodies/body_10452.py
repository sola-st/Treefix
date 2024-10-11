# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Optimized version of `broadcast_gradient_args` that caches results.

  This implementation avoids creating `broadcast_gradient_args` ops in the case
  that the input shapes are fully defined, and provides hints to the calling
  code that can be used to avoid creating reduction and reshaping ops.

  Args:
    x: The left input tensor to a broadcasting binary op.
    y: The right input tensor to a broadcasting binary op.
    grad: The incoming gradient tensor for a broadcasting binary op.

  Returns:
    A pair of tuples, containing:
      * A 3-tuple of broadcast information for x, containing:
        * The shape of x (as a tuple or Tensor).
        * The reduction indices for x (as a tuple or Tensor).
        * A boolean, which if True, indicates that x's shape differs from grad's
          shape (and so x's gradient must be reduced and/or reshaped).
      * A 3-tuple of broadcast information for y, containing the respective
        details for y.
  """
# NOTE: It may be productive to apply these optimizations in the eager case
# as well.
if context.executing_eagerly() or not (
    isinstance(x, ops.Tensor) and isinstance(y, ops.Tensor)
    and isinstance(grad, ops.Tensor)):
    sx = array_ops.shape(x)
    sy = array_ops.shape(y)
    rx, ry = gen_array_ops.broadcast_gradient_args(sx, sy)
    exit(((sx, rx, True), (sy, ry, True)))

# pylint: disable=protected-access
x_shape_tuple = x._shape_tuple()
y_shape_tuple = y._shape_tuple()
grad_shape_tuple = grad._shape_tuple()
# pylint: enable=protected-access

if (x_shape_tuple is None or None in x_shape_tuple or
    y_shape_tuple is None or None in y_shape_tuple):
    sx = array_ops.shape_internal(x, optimize=False)
    sy = array_ops.shape_internal(y, optimize=False)
    rx, ry = gen_array_ops.broadcast_gradient_args(sx, sy)
    exit(((sx, rx, True), (sy, ry, True)))

x_needs_reduction = x_shape_tuple != grad_shape_tuple
y_needs_reduction = y_shape_tuple != grad_shape_tuple

# Get the default graph rather than relying on `x.graph`, `y.graph`, or
# `grad.graph`, because these may be eager tensors.
g = ops.get_default_graph()

try:
    rx, ry = g._bcast_grad_args_cache[(x_shape_tuple, y_shape_tuple)]  # pylint: disable=protected-access
    exit(((x_shape_tuple, rx, x_needs_reduction), (
        y_shape_tuple, ry, y_needs_reduction)))
except KeyError:
    rx, ry = array_ops.broadcast_gradient_args(x_shape_tuple, y_shape_tuple)
    # TODO(mrry): If this becomes a bottleneck, add a multi-output version of
    # `TF_TryEvaluateConstant()`.
    rx_value = tuple(tensor_util.try_evaluate_constant(rx))
    assert rx_value is not None
    ry_value = tuple(tensor_util.try_evaluate_constant(ry))
    assert ry_value is not None
    g._bcast_grad_args_cache[(x_shape_tuple, y_shape_tuple)] = (  # pylint: disable=protected-access
        rx_value, ry_value)

    exit(((x_shape_tuple, rx_value, x_needs_reduction), (
        y_shape_tuple, ry_value, y_needs_reduction)))
