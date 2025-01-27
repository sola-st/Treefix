# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Implements support for handling RaggedTensors.

  Args:
    y_true: Tensor of one-hot true targets.
    y_pred: Tensor of predicted targets.
    from_logits: Whether `y_pred` is expected to be a logits tensor. By default,
      we assume that `y_pred` encodes a probability distribution.
    label_smoothing: Float in [0, 1]. If > `0` then smooth the labels. For
      example, if `0.1`, use `0.1 / num_classes` for non-target labels
      and `0.9 + 0.1 / num_classes` for target labels.
    axis: Axis along which to compute crossentropy.

  Returns:
    Binary crossentropy loss value.

  Expected shape: (batch, sequence_len) with sequence_len being variable
  per batch.
  Return shape: (batch,); returns the per batch mean of the loss values.

  When used by BinaryCrossentropy() with the default reduction
  (SUM_OVER_BATCH_SIZE), the reduction averages the per batch losses over
  the number of batches.
  """
fn = functools.partial(
    binary_crossentropy,
    from_logits=from_logits,
    label_smoothing=label_smoothing,
    axis=axis)
exit(_ragged_tensor_apply_loss(fn, y_true, y_pred))
