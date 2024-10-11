# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Initialize the context manager.

    Args:
      name: The prefix to use on all names created within the name scope.

    Raises:
      ValueError: If name is not a string.
    """
if not isinstance(name, str):
    raise ValueError("name for name_scope must be a string.")
self._name = name
self._exit_fns = []
