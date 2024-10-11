# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Add a callback to run when the default function graph goes out of scope.

  Usage:

  ```python
  @tf.function
  def fn(x, v):
    expensive = expensive_object(v)
    add_exit_callback_to_default_func_graph(lambda: expensive.release())
    return g(x, expensive)

  fn(x=tf.constant(...), v=...)
  # `expensive` has been released.
  ```

  Args:
    fn: A callable that takes no arguments and whose output is ignored.
      To be executed when exiting func graph scope.

  Raises:
    RuntimeError: If executed when the current default graph is not a FuncGraph,
      or not currently executing in function creation mode (e.g., if inside
      an init_scope).
  """
default_graph = get_default_graph()
if not default_graph._building_function:  # pylint: disable=protected-access
    raise RuntimeError(
        "Cannot add scope exit callbacks when not building a function.  "
        "Default graph: {}".format(default_graph))
default_graph._add_scope_exit_callback(fn)  # pylint: disable=protected-access
