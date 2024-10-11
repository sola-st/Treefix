# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/losses_utils.py
"""Computes the weighted loss.

  Args:
    losses: `Tensor` of shape `[batch_size, d1, ... dN]`.
    sample_weight: Optional `Tensor` whose rank is either 0, or the same rank as
      `losses`, or be broadcastable to `losses`.
    reduction: (Optional) Type of `tf.keras.losses.Reduction` to apply to loss.
      Default value is `SUM_OVER_BATCH_SIZE`.
    name: Optional name for the op.

  Raises:
    ValueError: If the shape of `sample_weight` is not compatible with `losses`.

  Returns:
    Weighted loss `Tensor` of the same type as `losses`. If `reduction` is
    `NONE`, this has the same shape as `losses`; otherwise, it is scalar.
  """
ReductionV2.validate(reduction)

# If this function is called directly, then we just default 'AUTO' to
# 'SUM_OVER_BATCH_SIZE'. Eg. Canned estimator use cases.
if reduction == ReductionV2.AUTO:
    reduction = ReductionV2.SUM_OVER_BATCH_SIZE
if sample_weight is None:
    sample_weight = 1.0
with backend.name_scope(name or 'weighted_loss'):
    # Save the `reduction` argument for loss normalization when distributing
    # to multiple replicas. Used only for estimator + v1 optimizer flow.
    ops.get_default_graph()._last_loss_reduction = reduction  # pylint: disable=protected-access

    if not isinstance(losses,
                      (keras_tensor.KerasTensor, ragged_tensor.RaggedTensor)):
        losses = ops.convert_to_tensor_v2_with_dispatch(losses)
    input_dtype = losses.dtype

    if not isinstance(sample_weight, keras_tensor.KerasTensor):
        sample_weight = ops.convert_to_tensor_v2_with_dispatch(sample_weight)

    # TODO(psv): Handle casting here in a better way, eg. if losses is float64
    # we do not want to lose precision.
    losses = math_ops.cast(losses, 'float32')
    sample_weight = math_ops.cast(sample_weight, 'float32')
    # Update dimensions of `sample_weight` to match with `losses` if possible.
    losses, _, sample_weight = squeeze_or_expand_dimensions(  # pylint: disable=unbalanced-tuple-unpacking
        losses, None, sample_weight)
    weighted_losses = math_ops.multiply(losses, sample_weight)

    # Apply reduction function to the individual weighted losses.
    loss = reduce_weighted_loss(weighted_losses, reduction)
    # Convert the result back to the input type.
    loss = math_ops.cast(loss, input_dtype)
    exit(loss)
