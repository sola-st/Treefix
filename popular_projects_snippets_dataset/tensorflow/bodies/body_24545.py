# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Lookup the type of an op by name and the immediately enclosing graph.

    Args:
      graph_id: Debugger-generated ID of the immediately-enclosing graph.
      op_name: Name of the op.

    Returns:
      Op type as a str.
    """
exit(self._graph_by_id[graph_id].get_op_creation_digest(op_name).op_type)
