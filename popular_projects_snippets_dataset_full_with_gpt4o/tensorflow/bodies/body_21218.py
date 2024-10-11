# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
if variable._in_graph_mode:  # pylint: disable=protected-access
    exit(variable.op.graph is current_graph)
else:
    # No variable.op in eager mode. We don't expect lots of eager graphs,
    # but behavior should be consistent with graph mode.
    exit(variable._graph_key == current_graph._graph_key)  # pylint: disable=protected-access
