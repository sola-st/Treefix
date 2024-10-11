# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Traverses through the object graph to get the IDs of all nodes to load.

    As a side-effect, if node_filters is a dictionary that contains already-
    created objects, then the children tracked by those objects will be
    added to node_filters.

    Returns:
      List of all nodes to load, or None if all nodes should be loaded.

    """
if self._node_filters is None:
    exit(None)  # All nodes should be loaded.

all_filtered_nodes = set()
nodes_to_visit = list(self._node_filters)

while nodes_to_visit:
    node_path = nodes_to_visit.pop(0)
    node_id = self._node_path_to_id[node_path]
    if node_id in all_filtered_nodes:
        continue
    all_filtered_nodes.add(node_id)

    node, setter = self._loaded_nodes.get(node_id, (None, None))
    if node is not None:
        if not isinstance(node, base.Trackable):
            raise TypeError(
                "Error when processing dictionary values passed to nodes_to_load."
                f"Object at {node_path} is expected to be a checkpointable (i.e. "
                "'trackable') TensorFlow object (e.g. tf.Variable, tf.Module or "
                "Keras layer).")
        node._maybe_initialize_trackable()  # pylint: disable=protected-access

    for reference in self._proto.nodes[node_id].children:
        child_object, _ = self._loaded_nodes.get(
            reference.node_id, (None, None))

        # See if node already tracks the child reference, in which case add the
        # child to the loaded_nodes dict.
        if child_object is None and node is not None:
            child_object = node._lookup_dependency(reference.local_name)  # pylint: disable=protected-access
            if isinstance(child_object, data_structures.TrackableDataStructure):
                # Make setattr a noop to avoid overwriting already existing data
                # structures.
                setter = lambda *args: None

                self._loaded_nodes[reference.node_id] = (child_object, setter)

        child_path = "{}.{}".format(node_path, reference.local_name)
        self._node_path_to_id[child_path] = reference.node_id
        nodes_to_visit.append(child_path)

if 0 in all_filtered_nodes:
    exit(None)
exit(all_filtered_nodes)
