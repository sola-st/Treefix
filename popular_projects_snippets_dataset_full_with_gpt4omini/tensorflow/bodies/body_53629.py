# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Initialize the context manager.

    Args:
      name: The name argument that is passed to the op function.
      default_name: The default name to use if the `name` argument is `None`.
      values: The list of `Tensor` arguments that are passed to the op function.

    Raises:
      TypeError: if `default_name` is passed in but not a string.
    """
if not (default_name is None or isinstance(default_name, str)):
    raise TypeError(
        "`default_name` type (%s) is not a string type. You likely meant to "
        "pass this into the `values` kwarg." % type(default_name))
self._name = default_name if name is None else name
self._default_name = default_name
self._values = values
