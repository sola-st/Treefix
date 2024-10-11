# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Returns a context manager that specifies the resource container to use.

    Overridden from `tf.Graph` to update both the init_scope container
    and the present inner container. This is necessary to make sure setting
    containers applies correctly both to created variables and to stateful
    ops.

    Args:
      container_name: container name string.

    Returns:
      A context manager for defining resource containers for stateful ops,
        yields the container name.
    """
original_container = self._container
# pylint: disable=protected-access
with ops.init_scope():
    original_init_container = ops.get_default_graph()._container
try:
    self._container = container_name
    with ops.init_scope():
        ops.get_default_graph()._container = container_name
    exit(self._container)
finally:
    self._container = original_container
    with ops.init_scope():
        ops.get_default_graph()._container = original_init_container
