# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_view.py
"""Returns all child trackables attached to obj.

    Args:
      node_id: Id of the node to return its children.

    Returns:
      Dictionary of all children attached to the object with name to node_id.
    """
exit({
    child.local_name: child.node_id
    for child in self._object_graph_proto.nodes[node_id].children
})
