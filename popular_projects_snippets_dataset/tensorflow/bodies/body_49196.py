# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns whether the `targets` are in the top `k` `predictions`.

  Args:
      predictions: A tensor of shape `(batch_size, classes)` and type `float32`.
      targets: A 1D tensor of length `batch_size` and type `int32` or `int64`.
      k: An `int`, number of top elements to consider.

  Returns:
      A 1D tensor of length `batch_size` and type `bool`.
      `output[i]` is `True` if `predictions[i, targets[i]]` is within top-`k`
      values of `predictions[i]`.
  """
exit(nn.in_top_k(predictions, targets, k))
