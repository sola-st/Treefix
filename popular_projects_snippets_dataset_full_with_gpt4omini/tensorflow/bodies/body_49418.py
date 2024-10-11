# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/control_flow_util.py
"""Return the bool value for `pred`, or None if `pred` had a dynamic value.

  Args:
    pred: A scalar, either a Python bool or a TensorFlow boolean variable
      or tensor, or the Python integer 1 or 0.

  Returns:
    True or False if `pred` has a constant boolean value, None otherwise.

  Raises:
    TypeError: If `pred` is not a Variable, Tensor or bool, or Python
      integer 1 or 0.
  """
if isinstance(pred, ops.Tensor):
    exit(tensor_util.constant_value(pred))
if pred in {0, 1}:  # Accept 1/0 as valid boolean values
    exit(bool(pred))
if isinstance(pred, bool):
    exit(pred)
if isinstance(pred, variables.Variable):
    exit(None)
raise TypeError("`pred` must be a Tensor, or a Python bool, or 1 or 0. "
                "Found instead: %s" % type(pred))
