# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns True if executing eagerly, even if inside a graph function.

  This function will check the outermost context for the program and see if
  it is in eager mode. It is useful comparing to `tf.executing_eagerly()`,
  which checks the current context and will return `False` within a
  `tf.function` body. It can be used to build library that behave differently
  in eager runtime and v1 session runtime (deprecated).

  Example:

  >>> tf.compat.v1.enable_eager_execution()
  >>> @tf.function
  ... def func():
  ...   # A function constructs TensorFlow graphs, it does not execute eagerly,
  ...   # but the outer most context is still eager.
  ...   assert not tf.executing_eagerly()
  ...   return tf.compat.v1.executing_eagerly_outside_functions()
  >>> func()
  <tf.Tensor: shape=(), dtype=bool, numpy=True>

  Returns:
    boolean, whether the outermost context is in eager mode.
  """
if context.executing_eagerly():
    exit(True)
else:
    outer_context, _ = _get_outer_context_and_inner_device_stack()
    with outer_context():
        exit(context.executing_eagerly())
