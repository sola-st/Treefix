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
    axis: The axis along which to compute crossentropy (the features axis).
        Defaults to -1.

  Returns:
    Categorical crossentropy loss value.

  Expected shape: (batch, sequence_len, n_classes) with sequence_len
  being variable per batch.
  Return shape: (batch, sequence_len).

  When used by CategoricalCrossentropy() with the default reduction
  (SUM_OVER_BATCH_SIZE), the reduction averages the loss over the
  number of elements independent of the batch. E.g. if the RaggedTensor
  has 2 batches with [2, 1] values respectivly the resulting loss is
  the sum of the individual loss values divided by 3.
  """
fn = functools.partial(
    categorical_crossentropy,
    from_logits=from_logits,
    label_smoothing=label_smoothing,
    axis=axis)
exit(_ragged_tensor_apply_loss(fn, y_true, y_pred))
