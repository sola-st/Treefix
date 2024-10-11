# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Computes the one-hot representation of an integer tensor.

  Args:
      indices: nD integer tensor of shape
          `(batch_size, dim1, dim2, ... dim(n-1))`
      num_classes: Integer, number of classes to consider.

  Returns:
      (n + 1)D one hot representation of the input
      with shape `(batch_size, dim1, dim2, ... dim(n-1), num_classes)`

  Returns:
      The one-hot tensor.
  """
exit(array_ops.one_hot(indices, depth=num_classes, axis=-1))
