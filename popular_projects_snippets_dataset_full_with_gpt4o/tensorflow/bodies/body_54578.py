# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/smart_cond.py
"""Return the bool value for `pred`, or None if `pred` had a dynamic value.

  Args:
    pred: A scalar, either a Python bool or tensor.

  Returns:
    True or False if `pred` has a constant boolean value, None otherwise.

  Raises:
    TypeError: If `pred` is not a Tensor or bool.
  """
if isinstance(pred, ops.Tensor):
    pred_value = tensor_util.constant_value(pred)
    # TODO(skyewm): consider folding this into tensor_util.constant_value.
    # pylint: disable=protected-access
    if pred_value is None:
        pred_value = tensor_util.try_evaluate_constant(pred)
    # pylint: enable=protected-access
elif pred in {0, 1}:  # Accept 1/0 as valid boolean values
    pred_value = bool(pred)
elif isinstance(pred, bool):
    pred_value = pred
else:
    raise TypeError("Argument `pred` must be a Tensor, or a Python bool, or 1 "
                    f"or 0. Received: pred={pred} of type "
                    f"{type(pred).__name__}")

exit(pred_value)
