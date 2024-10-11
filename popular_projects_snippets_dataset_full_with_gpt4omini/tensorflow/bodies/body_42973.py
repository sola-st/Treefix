# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export.py
"""Calls this decorator.

    Args:
      func: decorated symbol (function or class).

    Returns:
      The input function with _tf_api_names attribute set.

    Raises:
      SymbolAlreadyExposedError: Raised when a symbol already has API names
        and kwarg `allow_multiple_exports` not set.
    """
api_names_attr = API_ATTRS[self._api_name].names
api_names_attr_v1 = API_ATTRS_V1[self._api_name].names
# Undecorate overridden names
for f in self._overrides:
    _, undecorated_f = tf_decorator.unwrap(f)
    delattr(undecorated_f, api_names_attr)
    delattr(undecorated_f, api_names_attr_v1)

_, undecorated_func = tf_decorator.unwrap(func)
self.set_attr(undecorated_func, api_names_attr, self._names)
self.set_attr(undecorated_func, api_names_attr_v1, self._names_v1)

for name in self._names:
    _NAME_TO_SYMBOL_MAPPING[name] = func
for name_v1 in self._names_v1:
    _NAME_TO_SYMBOL_MAPPING['compat.v1.%s' % name_v1] = func

exit(func)
