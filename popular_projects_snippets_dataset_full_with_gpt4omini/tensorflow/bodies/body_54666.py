# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Builds the list of NodeDefs in the GraphDef.

    This list consists of all NodeDefs in the main graph as well as all control
    flow NodeDefs in the functions.

    The remaining NodeDefs in the functions are not included because the op
    names
    are not unique and the variables are handled differently than the main
    graph.
    The control flow ops need to be extracted because they are need their
    attributes to be updated similar to the control flow ops in the main graph.
    """
self._node_defs = {node.name: node for node in self._graph_def.node}

if self._graph_def.library:
    for func in self._graph_def.library.function:
        self._node_defs.update({
            node.name: node
            for node in func.node_def
            if node.op in _CONTROL_FLOW_OPS
        })
