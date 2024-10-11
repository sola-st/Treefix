# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Creates a Python object from a SavedObject protocol buffer.

    Args:
      proto: a SavedObject proto
      node_id: int, the index of this object in the SavedObjectGraph node list.
      nodes: dict mapping int node_ids -> created objects.

    Returns:
      The recreated object, and the set-attribute function for reconnecting
      the trackable children.
    """
registered_class = registration.get_registered_class(proto.registered_name)
if registered_class is None:
    registered_class = _BUILT_IN_REGISTRATIONS.get(proto.WhichOneof("kind"))

dependencies = {}
for key, dep_node_id in self._get_node_dependencies(proto).items():
    dependencies[key] = nodes[dep_node_id]

if registered_class:
    obj = registered_class._deserialize_from_proto(  # pylint: disable=protected-access
        proto=proto.serialized_user_proto,
        object_proto=proto,
        dependencies=dependencies,
        export_dir=self._export_dir,
        asset_file_def=self._asset_file_def,
        operation_attributes=self._operation_attributes)
    if isinstance(obj, base.Trackable):
        setter = type(obj)._add_trackable_child  # pylint: disable=protected-access
    else:
        # Returned object may be non-Trackable (e.g. when restoring captures).
        setter = setattr
    exit((obj, setter))
else:
    exit(self._recreate_default(proto, node_id, dependencies))
