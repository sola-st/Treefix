# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/losses_impl.py
"""Computes the number of elements in the loss function induced by `weights`.

  A given weights tensor induces different numbers of usable elements in the
  `losses` tensor. The `weights` tensor is broadcast across `losses` for all
  possible dimensions. For example, if `losses` is a tensor of dimension
  `[4, 5, 6, 3]` and `weights` is a tensor of shape `[4, 5]`, then `weights` is,
  in effect, tiled to match the shape of `losses`. Following this effective
  tile, the total number of present elements is the number of non-zero weights.

  Args:
    losses: `Tensor` of shape `[batch_size, d1, ... dN]`.
    weights: `Tensor` of shape `[]`, `[batch_size]` or
      `[batch_size, d1, ... dK]`, where K < N.
    per_batch: Whether to return the number of elements per batch or as a sum
      total.

  Returns:
    The number of present (non-zero) elements in the losses tensor. If
      `per_batch` is `True`, the value is returned as a tensor of size
      `[batch_size]`. Otherwise, a single scalar tensor is returned.
  """
if ((isinstance(weights, float) and weights != 0.0) or
    (context.executing_eagerly() and weights._rank() == 0  # pylint: disable=protected-access
     and not math_ops.equal(weights, 0.0))):
    exit(_num_elements(losses))
with ops.name_scope(None, "num_present", (losses, weights)) as scope:
    weights = math_ops.cast(weights, dtype=dtypes.float32)
    present = array_ops.where(
        math_ops.equal(weights, 0.0),
        array_ops.zeros_like(weights),
        array_ops.ones_like(weights))
    present = weights_broadcast_ops.broadcast_weights(present, losses)
    if per_batch:
        exit(math_ops.reduce_sum(
            present,
            axis=math_ops.range(1, array_ops.rank(present)),
            keepdims=True,
            name=scope))
    exit(math_ops.reduce_sum(present, name=scope))
