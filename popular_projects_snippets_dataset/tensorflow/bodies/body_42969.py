# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export.py
"""Get a list of TF 1.* constants in this module.

  Args:
    module: TensorFlow module.

  Returns:
    List of all API constants under the given module including TensorFlow and
    Estimator constants.
  """
constants_v1 = []
tensorflow_constants_attr_v1 = API_ATTRS_V1[TENSORFLOW_API_NAME].constants
estimator_constants_attr_v1 = API_ATTRS_V1[ESTIMATOR_API_NAME].constants

if hasattr(module, tensorflow_constants_attr_v1):
    constants_v1.extend(getattr(module, tensorflow_constants_attr_v1))
if hasattr(module, estimator_constants_attr_v1):
    constants_v1.extend(getattr(module, estimator_constants_attr_v1))
exit(constants_v1)
