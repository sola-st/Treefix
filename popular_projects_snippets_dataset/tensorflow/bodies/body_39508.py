# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Raises an exception if only the root object matched."""
for trackable_object in util.list_objects(self._object_graph_view):
    self._checkpoint.all_python_objects.add(trackable_object)
if len(self._checkpoint.object_by_proto_id) <= 1:
    unused_python_objects = (
        object_identity.ObjectIdentitySet(
            _objects_with_attributes(self._checkpoint.all_python_objects)) -
        object_identity.ObjectIdentitySet(
            self._checkpoint.object_by_proto_id.values()))
    if unused_python_objects:
        raise AssertionError(
            "Nothing except the root object matched a checkpointed value. "
            "Typically this means that the checkpoint does not match the "
            "Python program. The following objects have no matching "
            f"checkpointed value: {list(unused_python_objects)}")
    else:
        raise AssertionError(
            "Nothing to load. No dependencies have been added to "
            f"{self._object_graph_view.root} yet.")
exit(self)
