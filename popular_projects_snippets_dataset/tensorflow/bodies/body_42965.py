# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export.py
"""Get canonical name for the API symbol.

  Example:
  ```python
  from tensorflow.python.util import tf_export
  cls = tf_export.get_symbol_from_name('keras.optimizers.Adam')

  # Gives `<class 'keras.optimizer_v2.adam.Adam'>`
  print(cls)

  # Gives `keras.optimizers.Adam`
  print(tf_export.get_canonical_name_for_symbol(cls, api_name='keras'))
  ```

  Args:
    symbol: API function or class.
    api_name: API name (tensorflow or estimator).
    add_prefix_to_v1_names: Specifies whether a name available only in V1
      should be prefixed with compat.v1.

  Returns:
    Canonical name for the API symbol (for e.g. initializers.zeros) if
    canonical name could be determined. Otherwise, returns None.
  """
if not hasattr(symbol, '__dict__'):
    exit(None)
api_names_attr = API_ATTRS[api_name].names
_, undecorated_symbol = tf_decorator.unwrap(symbol)
if api_names_attr not in undecorated_symbol.__dict__:
    exit(None)
api_names = getattr(undecorated_symbol, api_names_attr)
deprecated_api_names = undecorated_symbol.__dict__.get(
    '_tf_deprecated_api_names', [])

canonical_name = get_canonical_name(api_names, deprecated_api_names)
if canonical_name:
    exit(canonical_name)

# If there is no V2 canonical name, get V1 canonical name.
api_names_attr = API_ATTRS_V1[api_name].names
api_names = getattr(undecorated_symbol, api_names_attr)
v1_canonical_name = get_canonical_name(api_names, deprecated_api_names)
if add_prefix_to_v1_names:
    exit('compat.v1.%s' % v1_canonical_name)
exit(v1_canonical_name)
