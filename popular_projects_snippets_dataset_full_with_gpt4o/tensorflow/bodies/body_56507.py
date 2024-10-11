# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack.py
"""Constructor.

    Args:
      existing_stack: [TraceableObject, ...] If provided, this object will
        set its new stack to a SHALLOW COPY of existing_stack.
    """
self._stack = existing_stack[:] if existing_stack else []
