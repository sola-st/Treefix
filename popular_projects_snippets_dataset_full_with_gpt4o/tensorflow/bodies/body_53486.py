# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Scope which defines a variable creation function.

    Args:
      creator: A callable taking `next_creator` and `kwargs`. See the
        `tf.variable_creator_scope` docstring.
      priority: Creators with a higher `priority` are called first. Within the
        same priority, creators are called inner-to-outer.

    Yields:
      `_variable_creator_scope` is a context manager with a side effect, but
      doesn't return a value.

    Raises:
      RuntimeError: If variable creator scopes are not properly nested.
    """
# This step keeps a reference to the existing stack, and it also initializes
# self._thread_local._variable_creator_stack if it doesn't exist yet.
old = self._variable_creator_stack
new = list(old)
new.append((priority, creator))
# Sorting is stable, so we'll put higher-priority creators later in the list
# but otherwise maintain registration order.
new.sort(key=lambda item: item[0])
self._thread_local._variable_creator_stack = new  # pylint: disable=protected-access
try:
    exit()
finally:
    if self._thread_local._variable_creator_stack is not new:  # pylint: disable=protected-access
        raise RuntimeError(
            "Exiting variable_creator_scope without proper nesting.")
    self._thread_local._variable_creator_stack = old  # pylint: disable=protected-access
