# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Utility function for transitioning to the new session API.

  Args:
    tensor_list: a list of `Tensor`s.

  Returns:
    A list of each `Tensor`s name (as byte arrays).
  """
exit([compat.as_bytes(t.name) for t in tensor_list])
