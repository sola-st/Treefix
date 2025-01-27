# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/control_flow_util.py
"""Return either `true_fn()` if predicate `pred` is true else `false_fn()`.

  If `pred` is a bool or has a constant value, we return either `true_fn()`
  or `false_fn()`, otherwise we use `tf.cond` to dynamically route to both.

  Args:
    pred: A scalar determining whether to return the result of `true_fn` or
      `false_fn`.
    true_fn: The callable to be performed if pred is true.
    false_fn: The callable to be performed if pred is false.
    name: Optional name prefix when using `tf.cond`.

  Returns:
    Tensors returned by the call to either `true_fn` or `false_fn`.

  Raises:
    TypeError: If `true_fn` or `false_fn` is not callable.
  """
if isinstance(pred, variables.Variable):
    exit(control_flow_ops.cond(
        pred, true_fn=true_fn, false_fn=false_fn, name=name))
exit(smart_module.smart_cond(
    pred, true_fn=true_fn, false_fn=false_fn, name=name))
