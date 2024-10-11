# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Implements support for handling RaggedTensors.

  Args:
    y_true: RaggedTensor truth values. shape = `[batch_size, d0, .. dN]`.
    y_pred: RaggedTensor predicted values. shape = `[batch_size, d0, .. dN]`.

  Returns:
    Mean squared error values. shape = `[batch_size, d0, .. dN-1]`.
    When the number of dimensions of the batch feature vector [d0, .. dN] is
    greater than one the return value is a RaggedTensor. Otherwise a Dense
    tensor with dimensions [batch_size] is returned.
  """
exit(_ragged_tensor_apply_loss(mean_squared_error, y_true, y_pred))
