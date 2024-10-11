# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Create the copied nodes and variables while traversing the nodes.

    This method performs a BFS to traverse the nodes while avoiding duplicated
    visits. Throughout the process, self._mapping, self._original_nodes, and
    self._var_pairs are populated.

    Args:
      to_traverse: A deque that stores the nodes to be traversed.
      visited: A list of nodes that have been visited.
    """
# pylint: disable=protected-access
while to_traverse:
    current_trackable = to_traverse.popleft()
    self._original_nodes.append(current_trackable)

    if isinstance(current_trackable, (Variable, ShardedVariable)):
        self._copy_trackable(current_trackable)
    if isinstance(current_trackable, TPUEmbedding):
        self._handle_tpu_embedding(current_trackable)

    for child in current_trackable._trackable_children().values():
        if child in visited:
            continue
        visited.add(child)
        to_traverse.append(child)
