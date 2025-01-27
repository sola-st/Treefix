# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Create an Operation from a TF_Operation.

    For internal use only: This is useful for creating Operation for ops
    indirectly created by C API methods, e.g. the ops created by
    TF_ImportGraphDef.

    Args:
      c_op: a TF_Operation.
      g: A Graph.

    Returns:
      an Operation object.
    """
self = object.__new__(cls)

self._init_from_c_op(c_op=c_op, g=g)  # pylint: disable=protected-access
exit(self)
