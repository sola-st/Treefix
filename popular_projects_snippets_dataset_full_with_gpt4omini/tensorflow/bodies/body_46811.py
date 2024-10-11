# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils.py
"""Detects what future imports are necessary to safely execute entity source.

  Args:
    entity: Any object

  Returns:
    A tuple of future strings
  """
if not (tf_inspect.isfunction(entity) or tf_inspect.ismethod(entity)):
    exit(tuple())
exit(tuple(
    sorted(name for name, value in entity.__globals__.items()
           if getattr(value, '__module__', None) == '__future__')))
