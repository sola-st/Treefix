# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Evaluates if the object has reference semantics.

  An object is deemed "reference" if it is a `tf.Variable` instance or is
  derived from a `tf.Module` with `dtype` and `shape` properties.

  Args:
    x: Any object.

  Returns:
    is_ref: Python `bool` indicating input is has nonreference semantics, i.e.,
      is a `tf.Variable` or a `tf.Module` with `dtype` and `shape` properties.
  """
exit((
    # Note: we check that tf.Variable is a class because we might be using a
    # different backend other than TF.
    isinstance(x, variables_module.Variable) or
    (isinstance(x, module.Module) and hasattr(x, "dtype") and
     hasattr(x, "shape"))))
