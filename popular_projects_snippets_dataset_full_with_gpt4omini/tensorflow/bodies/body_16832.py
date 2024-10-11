# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/losses_impl.py
"""Computes the weighted loss.

  Args:
    losses: `Tensor` of shape `[batch_size, d1, ... dN]`.
    weights: Optional `Tensor` whose rank is either 0, or the same rank as
      `losses`, and must be broadcastable to `losses` (i.e., all dimensions must
      be either `1`, or the same as the corresponding `losses` dimension).
    scope: the scope for the operations performed in computing the loss.
    loss_collection: the loss will be added to these collections.
    reduction: Type of reduction to apply to loss.

  Returns:
    Weighted loss `Tensor` of the same type as `losses`. If `reduction` is
    `NONE`, this has the same shape as `losses`; otherwise, it is scalar.

  Raises:
    ValueError: If `weights` is `None` or the shape is not compatible with
      `losses`, or if the number of dimensions (rank) of either `losses` or
      `weights` is missing.

  Note:
    When calculating the gradient of a weighted loss contributions from
    both `losses` and `weights` are considered. If your `weights` depend
    on some model parameters but you do not want this to affect the loss
    gradient, you need to apply `tf.stop_gradient` to `weights` before
    passing them to `compute_weighted_loss`.

  @compatibility(eager)
  The `loss_collection` argument is ignored when executing eagerly. Consider
  holding on to the return value or collecting losses via a `tf.keras.Model`.
  @end_compatibility
  """
Reduction.validate(reduction)
with ops.name_scope(scope, "weighted_loss", (losses, weights)):
    # Save the `reduction` argument for loss normalization when distributing
    # to multiple replicas. Used only for estimator + v1 optimizer flow.
    ops.get_default_graph()._last_loss_reduction = reduction  # pylint: disable=protected-access

    def compute_loss(losses, weights, loss_collection, reduction):
        losses = ops.convert_to_tensor(losses)
        input_dtype = losses.dtype
        losses = math_ops.cast(losses, dtype=dtypes.float32)
        weights = math_ops.cast(weights, dtype=dtypes.float32)
        weighted_losses = math_ops.multiply(losses, weights)
        if reduction == Reduction.NONE:
            loss = weighted_losses
        else:
            loss = math_ops.reduce_sum(weighted_losses)
            if reduction == Reduction.MEAN:
                loss = _safe_mean(
                    loss, math_ops.reduce_sum(array_ops.ones_like(losses) * weights))
            elif (reduction == Reduction.SUM_BY_NONZERO_WEIGHTS or
                  reduction == Reduction.SUM_OVER_NONZERO_WEIGHTS):
                loss = _safe_mean(loss, _num_present(losses, weights))
            elif reduction == Reduction.SUM_OVER_BATCH_SIZE:
                loss = _safe_mean(loss, _num_elements(losses))

      # Convert the result back to the input type.
        loss = math_ops.cast(loss, input_dtype)
        util.add_loss(loss, loss_collection)
        exit(loss)

    # Skip the assert_broadcastable in XLA context because asserts are not
    # supported so it only causes unnecessary ops. Also skip it because it uses
    # a DenseToDenseSetOperation op that is incompatible with XLA when
    # the shape(s) are dynamic.
    if control_flow_ops.get_enclosing_xla_context() is not None:
        exit(compute_loss(losses, weights, loss_collection, reduction))
    else:
        with ops.control_dependencies(
            (weights_broadcast_ops.assert_broadcastable(weights, losses),)):
            exit(compute_loss(losses, weights, loss_collection, reduction))
