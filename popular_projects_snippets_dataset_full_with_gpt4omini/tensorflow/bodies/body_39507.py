# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Asserts that trackable Python objects have been matched.

    Note that this is a weaker assertion than `assert_consumed`. It will only
    fail for existing Python objects which are (transitive) dependencies of the
    root object and which do not have an entry in the checkpoint.

    It will not fail, for example, if a `tf.keras.Layer` object has not yet been
    built and so has not created any `tf.Variable` objects.

    Returns:
      `self` for chaining.

    Raises:
      AssertionError: If a Python object exists in the transitive dependencies
        of the root object but does not have a value in the checkpoint.
    """
for node_id, node in enumerate(self._checkpoint.object_graph_proto.nodes):
    trackable = self._checkpoint.object_by_proto_id.get(node_id, None)
    if (trackable is not None and
        trackable._update_uid < self._checkpoint.restore_uid):  # pylint: disable=protected-access
        raise AssertionError(
            f"Object {node} not assigned a value from checkpoint.")
for trackable_object in util.list_objects(self._object_graph_view):
    # Remove data structures that do not contain any variables from
    # restoration checks.
    if (isinstance(trackable_object,
                   data_structures.TrackableDataStructure) and
        not trackable_object._trackable_children()):  # pylint: disable=protected-access
        continue
    self._checkpoint.all_python_objects.add(trackable_object)
unused_python_objects = (
    object_identity.ObjectIdentitySet(
        _objects_with_attributes(
            self._checkpoint.all_python_objects)) -
    object_identity.ObjectIdentitySet(
        self._checkpoint.object_by_proto_id.values()))
if unused_python_objects:
    num_unused_python_objects = len(list(unused_python_objects))
    # Display max number of 10 variables in error message.
    num_variables_to_show = min(10, num_unused_python_objects)
    raise AssertionError(
        f"Found {num_unused_python_objects} Python objects that were "
        "not bound to checkpointed values, likely due to changes in the "
        f"Python program. Showing {num_variables_to_show} of "
        f"{num_unused_python_objects} unmatched objects: "
        f"{list(unused_python_objects)[:num_variables_to_show]}")
exit(self)
