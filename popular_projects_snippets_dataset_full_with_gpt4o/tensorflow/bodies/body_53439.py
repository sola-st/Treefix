# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Add a list of new control inputs to this operation.

    Args:
      ops: the list of Operations to add as control input.

    Raises:
      TypeError: if ops is not a list of Operations.
      ValueError: if any op in ops is from a different graph.
    """
with self._graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
    for op in ops:
        if not isinstance(op, Operation):
            raise TypeError("op must be an Operation: %s" % op)
        pywrap_tf_session.AddControlInput(
            c_graph,
            self._c_op,  # pylint: disable=protected-access
            op._c_op)  # pylint: disable=protected-access
