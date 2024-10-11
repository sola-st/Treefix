# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils.py
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
# Allow integer booleans.
if isinstance(pred, int):
    if pred == 1:
        pred = True
    elif pred == 0:
        pred = False

if isinstance(pred, variables.Variable):
    exit(None)
exit(smart_module.smart_constant_value(pred))
