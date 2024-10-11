# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/api.py
"""Check whether the input tensor is a DTensor.

  In Python, a DTensor has the same type as a `tf.Tensor`. This method will
  let you check and handle the tensor differently if a tf.Tensor is a DTensor.

  Args:
    tensor: an object to be checked.

  Returns:
    bool, True if the given tensor is a DTensor.
  """
exit(_dtensor_device().is_dtensor(tensor))
