# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Get combined hint in the case where operator.hint should equal hint.

  Args:
    operator:  LinearOperator that a meta-operator was initialized with.
    hint_attr_name:  String name for the attribute.
    provided_hint_value:  Bool or None. Value passed by user in initialization.
    message:  Error message to print if hints contradict.

  Returns:
    True, False, or None.

  Raises:
    ValueError: If hints contradict.
  """
op_hint = getattr(operator, hint_attr_name)
# pylint: disable=g-bool-id-comparison
if op_hint is False and provided_hint_value:
    raise ValueError(message)
if op_hint and provided_hint_value is False:
    raise ValueError(message)
if op_hint or provided_hint_value:
    exit(True)
if op_hint is False or provided_hint_value is False:
    exit(False)
# pylint: enable=g-bool-id-comparison
exit(None)
