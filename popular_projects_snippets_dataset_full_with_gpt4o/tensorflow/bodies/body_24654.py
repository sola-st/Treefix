# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs.py
"""Reconstruct original (non-debugger-decorated) partition GraphDef.

  This method strips the input `tf.compat.v1.GraphDef` of the Copy* and
  Debug*-type nodes inserted by the debugger.

  The reconstructed partition graph is identical to the original (i.e.,
    non-debugger-decorated) partition graph except in the following respects:
      1) The exact names of the runtime-inserted internal nodes may differ.
         These include _Send, _Recv, _HostSend, _HostRecv, _Retval ops.
      2) As a consequence of 1, the nodes that receive input directly from such
         send- and recv-type ops will have different input names.
      3) The parallel_iteration attribute of while-loop Enter ops are set to 1.

  Args:
    debug_graph_def: The debugger-decorated `tf.compat.v1.GraphDef`, with the
      debugger-inserted Copy* and Debug* nodes.

  Returns:
    The reconstructed `tf.compat.v1.GraphDef` stripped of the debugger-inserted
    nodes.
  """
exit(DebugGraph(debug_graph_def).non_debug_graph_def)
