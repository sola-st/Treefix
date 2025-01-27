# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the function definition for 'name'.

    Args:
      name: string function name.

    Returns:
      The function def proto.
    """
exit(self._functions.get(compat.as_str(name), None))
