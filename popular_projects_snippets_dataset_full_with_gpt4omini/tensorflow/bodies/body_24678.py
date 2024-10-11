# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_server.py
"""Get the list of debug watches with attribute gated_grpc=True.

    Since the server receives `GraphDef` from the debugged runtime, it can only
    return such debug watches that it has received so far.

    Returns:
      A `list` of `DebugWatch` `namedtuples` representing the debug watches with
      gated_grpc=True. Each `namedtuple` element has the attributes:
        `node_name` as a `str`,
        `output_slot` as an `int`,
        `debug_op` as a `str`.
    """
exit(list(self._gated_grpc_debug_watches))
