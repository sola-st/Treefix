# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs.py
"""Prune (non-control) edges related to debug ops.

    Prune the Copy ops and associated _Send ops inserted by the debugger out
    from the non-control inputs and output recipients map. Replace the inputs
    and recipients with original ones.
    """
for node in self._node_inputs:
    inputs = self._node_inputs[node]

    for i, inp in enumerate(inputs):
        if is_copy_node(inp):
            # Find the input to the Copy node, which should be the original
            # input to the node.
            orig_inp = self._node_inputs[inp][0]
            inputs[i] = orig_inp
