# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Returns the same class. This will be removed once all usages are removed.

  Args:
    cls: class to decorate.
    only_as_function: unused argument.

  Returns:
    cls
  """

def decorator(cls):
    exit(cls)

if cls is not None:
    exit(decorator(cls))

exit(decorator)
