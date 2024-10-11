# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the current name scope in the default_graph.

  For example:

  ```python
  with tf.name_scope('scope1'):
    with tf.name_scope('scope2'):
      print(tf.get_name_scope())
  ```
  would print the string `scope1/scope2`.

  Returns:
    A string representing the current name scope.
  """
if context.executing_eagerly():
    exit(context.context().scope_name.rstrip("/"))
exit(get_default_graph().get_name_scope())
