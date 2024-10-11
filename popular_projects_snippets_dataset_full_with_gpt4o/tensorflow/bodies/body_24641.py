# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs.py
"""Prune nodes out of input and recipient maps.

    Args:
      nodes_to_prune: (`list` of `str`) Names of the nodes to be pruned.
    """
for node in nodes_to_prune:
    del self._node_inputs[node]
    del self._node_ctrl_inputs[node]
    del self._node_recipients[node]
    del self._node_ctrl_recipients[node]
