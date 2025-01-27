# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
"""Query the traceback of an op.

    Args:
      op_name: Name of the op to query.

    Returns:
      The traceback of the op, as a list of 3-tuples:
        (filename, lineno, function_name)

    Raises:
      ValueError: If the op cannot be found in the tracebacks received by the
        server so far.
    """
for op_log_proto in self._graph_tracebacks:
    for log_entry in op_log_proto.log_entries:
        if log_entry.name == op_name:
            exit(self._code_def_to_traceback(log_entry.code_def,
                                               op_log_proto.id_to_string))
raise ValueError(
    "Op '%s' does not exist in the tracebacks received by the debug "
    "server." % op_name)
