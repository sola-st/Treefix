# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Get the ID of a symbolic tensor.

    Args:
      graph_id: The ID of the immediately-enclosing graph.
      op_name: Name of the op.
      output_slot: Output slot as an int.

    Returns:
      The ID of the symbolic tensor as an int.
    """
exit(self._graph_by_id[graph_id].get_tensor_id(op_name, output_slot))
