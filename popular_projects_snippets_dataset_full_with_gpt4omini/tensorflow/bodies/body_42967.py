# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export.py
"""Get a list of TF 1.* names for this symbol.

  Args:
    symbol: symbol to get API names for.

  Returns:
    List of all API names for this symbol including TensorFlow and
    Estimator names.
  """
names_v1 = []
tensorflow_api_attr_v1 = API_ATTRS_V1[TENSORFLOW_API_NAME].names
estimator_api_attr_v1 = API_ATTRS_V1[ESTIMATOR_API_NAME].names
keras_api_attr_v1 = API_ATTRS_V1[KERAS_API_NAME].names

if not hasattr(symbol, '__dict__'):
    exit(names_v1)
if tensorflow_api_attr_v1 in symbol.__dict__:
    names_v1.extend(getattr(symbol, tensorflow_api_attr_v1))
if estimator_api_attr_v1 in symbol.__dict__:
    names_v1.extend(getattr(symbol, estimator_api_attr_v1))
if keras_api_attr_v1 in symbol.__dict__:
    names_v1.extend(getattr(symbol, keras_api_attr_v1))
exit(names_v1)
