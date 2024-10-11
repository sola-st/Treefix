# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Clears the default graph stack and resets the global default graph.

  NOTE: The default graph is a property of the current thread. This
  function applies only to the current thread.  Calling this function while
  a `tf.compat.v1.Session` or `tf.compat.v1.InteractiveSession` is active will
  result in undefined
  behavior. Using any previously created `tf.Operation` or `tf.Tensor` objects
  after calling this function will result in undefined behavior.

  @compatibility(TF2)
  `reset_default_graph` does not work with either eager execution or
  `tf.function`, and you should not invoke it directly. To migrate code that
  uses Graph-related functions to TF2, rewrite the code without them. See the
  [migration guide](https://www.tensorflow.org/guide/migrate) for more
  description about the behavior and semantic changes between Tensorflow 1 and
  Tensorflow 2.
  @end_compatibility

  Raises:
    AssertionError: If this function is called within a nested graph.
  """
if not _default_graph_stack.is_cleared():
    raise AssertionError("Do not use tf.reset_default_graph() to clear "
                         "nested graphs. If you need a cleared graph, "
                         "exit the nesting and create a new graph.")
_default_graph_stack.reset()
