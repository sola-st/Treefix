# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/selective_registration_header_lib.py
"""Gets the ops and kernels needed from the tensorflow model."""
ops = set()
ops.update(_get_ops_from_nodedefs(graph_def.node))

for function in graph_def.library.function:
    ops.update(_get_ops_from_nodedefs(function.node_def))
exit(ops)
