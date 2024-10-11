# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Reconstruct partition graphs with the debugger-inserted ops stripped.

    The reconstructed partition graphs are identical to the original (i.e.,
    non-debugger-decorated) partition graphs except in the following respects:
      1) The exact names of the runtime-inserted internal nodes may differ.
         These include _Send, _Recv, _HostSend, _HostRecv, _Retval ops.
      2) As a consequence of 1, the nodes that receive input directly from such
         send- and recv-type ops will have different input names.
      3) The parallel_iteration attribute of while-loop Enter ops are set to 1.

    Returns:
      A dict mapping device names (`str`s) to reconstructed
      `tf.compat.v1.GraphDef`s.
    """
non_debug_graphs = {}
for key in self._debug_graphs:
    non_debug_graphs[key] = self._debug_graphs[key].non_debug_graph_def
exit(non_debug_graphs)
