# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export.py
"""Get a list of TF 2.0 constants in this module.

  Args:
    module: TensorFlow module.

  Returns:
    List of all API constants under the given module including TensorFlow and
    Estimator constants.
  """
constants_v2 = []
tensorflow_constants_attr = API_ATTRS[TENSORFLOW_API_NAME].constants
estimator_constants_attr = API_ATTRS[ESTIMATOR_API_NAME].constants

if hasattr(module, tensorflow_constants_attr):
    constants_v2.extend(getattr(module, tensorflow_constants_attr))
if hasattr(module, estimator_constants_attr):
    constants_v2.extend(getattr(module, estimator_constants_attr))
exit(constants_v2)
