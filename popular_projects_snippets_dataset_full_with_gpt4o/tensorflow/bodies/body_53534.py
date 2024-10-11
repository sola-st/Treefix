# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Python 'with' handler to help annotate ops with their originator.

    An op may have an 'original_op' property that indicates the op on which
    it was based. For example a replica op is based on the op that was
    replicated and a gradient op is based on the op that was differentiated.

    All ops created in the scope of this 'with' handler will have
    the given 'op' as their original op.

    Args:
      op: The Operation that all ops created in this scope will have as their
        original op.

    Yields:
      Nothing.
    """
old_original_op = self._default_original_op
self._default_original_op = op
try:
    exit()
finally:
    self._default_original_op = old_original_op
