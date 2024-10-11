# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Add an op creation data object.

    Args:
      graph_op_creation_digest: A GraphOpCreationDigest data object describing
        the creation of an op inside this graph.
    """
if graph_op_creation_digest.op_name in self._op_by_name:
    raise ValueError(
        "Duplicate op name: %s (op type: %s)" %
        (graph_op_creation_digest.op_name, graph_op_creation_digest.op_type))
self._op_by_name[
    graph_op_creation_digest.op_name] = graph_op_creation_digest
