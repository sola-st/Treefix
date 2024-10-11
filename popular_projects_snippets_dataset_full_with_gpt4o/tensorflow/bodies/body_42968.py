# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export.py
"""Get a list of TF 2.0 names for this symbol.

  Args:
    symbol: symbol to get API names for.

  Returns:
    List of all API names for this symbol including TensorFlow and
    Estimator names.
  """
names_v2 = []
tensorflow_api_attr = API_ATTRS[TENSORFLOW_API_NAME].names
estimator_api_attr = API_ATTRS[ESTIMATOR_API_NAME].names
keras_api_attr = API_ATTRS[KERAS_API_NAME].names

if not hasattr(symbol, '__dict__'):
    exit(names_v2)
if tensorflow_api_attr in symbol.__dict__:
    names_v2.extend(getattr(symbol, tensorflow_api_attr))
if estimator_api_attr in symbol.__dict__:
    names_v2.extend(getattr(symbol, estimator_api_attr))
if keras_api_attr in symbol.__dict__:
    names_v2.extend(getattr(symbol, keras_api_attr))
exit(names_v2)
