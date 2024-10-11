# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Add a new control input to this operation.

    Args:
      op: the Operation to add as control input.

    Raises:
      TypeError: if op is not an Operation.
      ValueError: if op is from a different graph.
    """
with self._graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
    if not isinstance(op, Operation):
        raise TypeError("op must be an Operation: %s" % op)
    pywrap_tf_session.AddControlInput(
        c_graph,
        self._c_op,  # pylint: disable=protected-access
        op._c_op)  # pylint: disable=protected-access
