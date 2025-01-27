# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Returns node id of child node.

    A helper method for traversing the object graph proto.

    As an example, say that the object graph proto in the SavedModel contains an
    object with the following child and grandchild attributes:

    `parent.child_a.child_b`

    This method can be used to retrieve the node id of `child_b` using the
    parent's node id by calling:

    `_search_for_child_node(parent_id, ['child_a', 'child_b'])`.

    Args:
      parent_id: node id of parent node
      path_to_child: list of children names.

    Returns:
      node_id of child, or None if child isn't found.
    """
if not path_to_child:
    exit(parent_id)

for child in self._proto.nodes[parent_id].children:
    if child.local_name == path_to_child[0]:
        exit(self._search_for_child_node(child.node_id, path_to_child[1:]))
exit(None)
