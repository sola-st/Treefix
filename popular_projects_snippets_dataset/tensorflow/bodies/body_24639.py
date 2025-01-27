# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs.py
"""Prune control edges related to the debug ops."""
for node in self._node_ctrl_inputs:
    ctrl_inputs = self._node_ctrl_inputs[node]
    debug_op_inputs = []
    for ctrl_inp in ctrl_inputs:
        if is_debug_node(ctrl_inp):
            debug_op_inputs.append(ctrl_inp)
    for debug_op_inp in debug_op_inputs:
        ctrl_inputs.remove(debug_op_inp)
