# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
""" Implements support for handling RaggedTensors.

      Expected y_pred shape: (batch, sequence_len, n_classes) with sequence_len
      being variable per batch.
      Return shape: (batch, sequence_len).

      When used by SparseCategoricalCrossentropy() with the default reduction
      (SUM_OVER_BATCH_SIZE), the reduction averages the loss over the
      number of elements independent of the batch. E.g. if the RaggedTensor
      has 2 batches with [2, 1] values respectively, the resulting loss is
      the sum of the individual loss values divided by 3.
  """
fn = functools.partial(
    sparse_categorical_crossentropy, from_logits=from_logits, axis=axis)
exit(_ragged_tensor_apply_loss(fn, y_true, y_pred, y_pred_extra_dim=True))
