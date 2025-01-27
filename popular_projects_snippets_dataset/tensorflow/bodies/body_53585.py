# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Wrapper for `Graph.container()` using the default graph.

  Args:
    container_name: The container string to use in the context.

  Returns:
    A context manager that specifies the default container to use for newly
    created stateful ops.
  """
exit(get_default_graph().container(container_name))
