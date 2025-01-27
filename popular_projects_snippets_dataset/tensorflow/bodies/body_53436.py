# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Fast path to set device if the type is known to be a string.

    This function is called frequently enough during graph construction that
    there are non-trivial performance gains if the caller can guarantee that
    the specified device is already a string.

    Args:
      device_str: A string specifying where to place this op.
    """
with self._graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
    pywrap_tf_session.SetRequestedDevice(
        c_graph,
        self._c_op,  # pylint: disable=protected-access
        device_str)
