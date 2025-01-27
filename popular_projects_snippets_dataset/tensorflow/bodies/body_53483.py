# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the name of an op given the name of its scope.

  Args:
    name: the name of the scope.

  Returns:
    the name of the op (equal to scope name minus any trailing slash).
  """
exit(name[:-1] if (name and name[-1] == "/") else name)
