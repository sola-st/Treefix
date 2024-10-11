# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Class decorator that registers a type for use with type-based dispatch.

  Should *not* be used with subclasses of `CompositeTensor` or `ExtensionType`
  (which are automatically registered).

  Note: this function is intended to support internal legacy use cases (such
  as RaggedTensorValue), and will probably not be exposed as a public API.

  Args:
    cls: The class to register.

  Returns:
    `cls`.
  """
_api_dispatcher.register_dispatchable_type(cls)
exit(cls)
