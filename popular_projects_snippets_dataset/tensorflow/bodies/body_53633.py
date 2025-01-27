# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Initialize the context manager.

    Args:
      name: The name argument that is passed to the op function.
      default_name: The default name to use if the `name` argument is `None`.
      values: The list of `Tensor` arguments that are passed to the op function.

    Raises:
      TypeError: if `default_name` is passed in but not a string.
    """
self._name_scope = name_scope(
    name, default_name, values, skip_on_eager=False)
self._name = default_name if name is None else name
