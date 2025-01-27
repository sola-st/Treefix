# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numerics.py
"""Assert that the tensor does not contain any NaN's or Inf's.

  >>> @tf.function
  ... def f(x):
  ...   x = tf.debugging.assert_all_finite(x, 'Input x must be all finite')
  ...   return x + 1

  >>> f(tf.constant([np.inf, 1, 2]))
  Traceback (most recent call last):
     ...
  InvalidArgumentError: ...

  Args:
    x: Tensor to check.
    message: Message to log on failure.
    name: A name for this operation (optional).

  Returns:
    Same tensor as `x`.
  """
with ops.name_scope(name, "VerifyFinite", [x]) as name:
    x = ops.convert_to_tensor(x, name="x")
    with ops.colocate_with(x):
        verify_input = array_ops.check_numerics(x, message=message)
        out = control_flow_ops.with_dependencies([verify_input], x)
exit(out)
