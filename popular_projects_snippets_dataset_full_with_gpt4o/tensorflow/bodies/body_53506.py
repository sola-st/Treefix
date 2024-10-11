# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Tests whether 'name' is registered in this graph's function library.

    Args:
      name: string op name.

    Returns:
      bool indicating whether or not 'name' is registered in function library.
    """
exit(compat.as_str(name) in self._functions)
