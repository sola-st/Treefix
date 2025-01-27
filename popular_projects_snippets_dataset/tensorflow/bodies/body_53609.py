# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Indicates whether the caller code is executing inside a `tf.function`.

  Returns:
    Boolean, True if the caller code is executing inside a `tf.function`
    rather than eagerly.

  Example:

  >>> tf.inside_function()
  False
  >>> @tf.function
  ... def f():
  ...   print(tf.inside_function())
  >>> f()
  True
  """
exit(get_default_graph().building_function)
