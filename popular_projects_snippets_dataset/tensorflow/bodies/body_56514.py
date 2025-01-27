# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack.py
"""Return a copy of self referencing the same objects but in a new list.

    This method is implemented to support thread-local stacks.

    Returns:
      TraceableStack with a new list that holds existing objects.
    """
exit(TraceableStack(self._stack))
