# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/losses_impl.py
"""Creates a cross-entropy loss using tf.nn.sigmoid_cross_entropy_with_logits.

  `weights` acts as a coefficient for the loss. If a scalar is provided,
  then the loss is simply scaled by the given value. If `weights` is a
  tensor of shape `[batch_size]`, then the loss weights apply to each
  corresponding sample.

  If `label_smoothing` is nonzero, smooth the labels towards 1/2:

      new_multiclass_labels = multiclass_labels * (1 - label_smoothing)
                              + 0.5 * label_smoothing

  Args:
    multi_class_labels: `[batch_size, num_classes]` target integer labels in
      `{0, 1}`.
    logits: Float `[batch_size, num_classes]` logits outputs of the network.
    weights: Optional `Tensor` whose rank is either 0, or the same rank as
    `multi_class_labels`, and must be broadcastable to `multi_class_labels`
    (i.e., all dimensions must be either `1`, or the same as the
    corresponding `losses` dimension).
    label_smoothing: If greater than `0` then smooth the labels.
    scope: The scope for the operations performed in computing the loss.
    loss_collection: collection to which the loss will be added.
    reduction: Type of reduction to apply to loss.

  Returns:
    Weighted loss `Tensor` of the same type as `logits`. If `reduction` is
    `NONE`, this has the same shape as `logits`; otherwise, it is scalar.

  Raises:
    ValueError: If the shape of `logits` doesn't match that of
      `multi_class_labels` or if the shape of `weights` is invalid, or if
      `weights` is None.  Also if `multi_class_labels` or `logits` is None.

  @compatibility(eager)
  The `loss_collection` argument is ignored when executing eagerly. Consider
  holding on to the return value or collecting losses via a `tf.keras.Model`.
  @end_compatibility
  """
if multi_class_labels is None:
    raise ValueError("Argument `multi_class_labels` must not be None.")
if logits is None:
    raise ValueError("Argument `logits` must not be None.")
with ops.name_scope(scope, "sigmoid_cross_entropy_loss",
                    (logits, multi_class_labels, weights)) as scope:
    logits = ops.convert_to_tensor(logits)
    multi_class_labels = math_ops.cast(multi_class_labels, logits.dtype)
    logits.get_shape().assert_is_compatible_with(multi_class_labels.get_shape())

    if label_smoothing > 0:
        multi_class_labels = (multi_class_labels * (1 - label_smoothing) +
                              0.5 * label_smoothing)

    losses = nn.sigmoid_cross_entropy_with_logits(labels=multi_class_labels,
                                                  logits=logits,
                                                  name="xentropy")
    exit(compute_weighted_loss(
        losses, weights, scope, loss_collection, reduction=reduction))
