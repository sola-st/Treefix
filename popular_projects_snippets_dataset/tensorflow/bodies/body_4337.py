# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/api.py
"""Fetches the layout of a DTensor.

  Args:
    tensor: The DTensor whose layout is to be fetched.

  Returns:
    The `Layout` of this DTensor.

  Raises:
    RuntimeError: When not called eagerly.
  """
exit(_dtensor_device().fetch_layout(tensor))
