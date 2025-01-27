# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/losses_impl.py
"""Adds a [Huber Loss](https://en.wikipedia.org/wiki/Huber_loss) term to the training procedure.

  For each value x in `error=labels-predictions`, the following is calculated:

  ```
    0.5 * x^2                  if |x| <= d
    0.5 * d^2 + d * (|x| - d)  if |x| > d
  ```

  where d is `delta`.

  `weights` acts as a coefficient for the loss. If a scalar is provided, then
  the loss is simply scaled by the given value. If `weights` is a tensor of size
  `[batch_size]`, then the total loss for each sample of the batch is rescaled
  by the corresponding element in the `weights` vector. If the shape of
  `weights` matches the shape of `predictions`, then the loss of each
  measurable element of `predictions` is scaled by the corresponding value of
  `weights`.

  Args:
    labels: The ground truth output tensor, same dimensions as 'predictions'.
    predictions: The predicted outputs.
    weights: Optional `Tensor` whose rank is either 0, or the same rank as
      `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
      be either `1`, or the same as the corresponding `losses` dimension).
    delta: `float`, the point where the huber loss function changes from a
      quadratic to linear.
    scope: The scope for the operations performed in computing the loss.
    loss_collection: collection to which the loss will be added.
    reduction: Type of reduction to apply to loss.

  Returns:
    Weighted loss float `Tensor`. If `reduction` is `NONE`, this has the same
    shape as `labels`; otherwise, it is scalar.

  Raises:
    ValueError: If the shape of `predictions` doesn't match that of `labels` or
      if the shape of `weights` is invalid.  Also if `labels` or
     `predictions` is None.

  @compatibility(eager)
  The `loss_collection` argument is ignored when executing eagerly. Consider
  holding on to the return value or collecting losses via a `tf.keras.Model`.
  @end_compatibility
  """
if labels is None:
    raise ValueError("Argument `labels` must not be None.")
if predictions is None:
    raise ValueError("Argument `predictions` must not be None.")
with ops.name_scope(scope, "huber_loss",
                    (predictions, labels, weights)) as scope:
    predictions = math_ops.cast(predictions, dtype=dtypes.float32)
    labels = math_ops.cast(labels, dtype=dtypes.float32)
    predictions.get_shape().assert_is_compatible_with(labels.get_shape())
    error = math_ops.subtract(predictions, labels)
    abs_error = math_ops.abs(error)
    quadratic = math_ops.minimum(abs_error, delta)
    # The following expression is the same in value as
    # tf.maximum(abs_error - delta, 0), but importantly the gradient for the
    # expression when abs_error == delta is 0 (for tf.maximum it would be 1).
    # This is necessary to avoid doubling the gradient, since there is already a
    # nonzero contribution to the gradient from the quadratic term.
    linear = math_ops.subtract(abs_error, quadratic)
    losses = math_ops.add(
        math_ops.multiply(
            ops.convert_to_tensor(0.5, dtype=quadratic.dtype),
            math_ops.multiply(quadratic, quadratic)),
        math_ops.multiply(delta, linear))
    exit(compute_weighted_loss(
        losses, weights, scope, loss_collection, reduction=reduction))
