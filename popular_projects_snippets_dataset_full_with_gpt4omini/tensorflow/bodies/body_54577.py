# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/smart_cond.py
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
if not callable(true_fn):
    raise TypeError(f"Argument `true_fn` must be callable. Received {true_fn}")
if not callable(false_fn):
    raise TypeError(
        f"Argument `false_fn` must be callable. Received {false_fn}")

pred_value = smart_constant_value(pred)
if pred_value is not None:
    if pred_value:
        exit(true_fn())
    else:
        exit(false_fn())
else:
    exit(control_flow_ops.cond(pred, true_fn=true_fn, false_fn=false_fn,
                                 name=name))
