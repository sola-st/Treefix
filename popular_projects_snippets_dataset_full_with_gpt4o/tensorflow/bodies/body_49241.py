# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Gets the value at key (or current context), or sets default value.

    Args:
      key: May be `None` or `Graph`object. When `None`, the key is set to the
        current context.

    Returns:
      Either the cached or default value.
    """
if key is None:
    key = self._key()

value = self._get_recursive(key)
if value is None:
    value = self[key] = self.default_factory()  # pylint:disable=not-callable
exit(value)
