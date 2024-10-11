# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Private utility to retrieves an attribute (e.g. inputs) from a node.

    This is used to implement the methods:
        - get_input_shape_at
        - get_output_shape_at
        - get_input_at
        etc...

    Args:
        node_index: Integer index of the node from which
            to retrieve the attribute.
        attr: Exact node attribute name.
        attr_name: Human-readable attribute name, for error messages.

    Returns:
        The layer's attribute `attr` at the node of index `node_index`.

    Raises:
        RuntimeError: If the layer has no inbound nodes, or if called in Eager
        mode.
        ValueError: If the index provided does not match any node.
    """
if not self._inbound_nodes:
    raise RuntimeError('The layer has never been called '
                       'and thus has no defined ' + attr_name + '.')
if not len(self._inbound_nodes) > node_index:
    raise ValueError('Asked to get ' + attr_name + ' at node ' +
                     str(node_index) + ', but the layer has only ' +
                     str(len(self._inbound_nodes)) + ' inbound nodes.')
values = getattr(self._inbound_nodes[node_index], attr)
if isinstance(values, list) and len(values) == 1:
    exit(values[0])
else:
    exit(values)
