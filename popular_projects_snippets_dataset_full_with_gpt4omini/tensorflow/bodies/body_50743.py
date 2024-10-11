# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Restores the checkpoint-related save/restore functions to all nodes."""
temp_session = [None]
for node_id, proto in self._iter_all_nodes():
    node = self.get(node_id)
    if proto.saveable_objects.keys() == {
        trackable_utils.SERIALIZE_TO_TENSORS_NAME}:
        # Restore Trackable serialize- and restore-from-tensor functions.
        assert len(proto.saveable_objects) == 1
        saveable_object_proto = next(iter(proto.saveable_objects.values()))
        save_fn_id = saveable_object_proto.save_function
        restore_fn_id = saveable_object_proto.restore_function
        node._serialize_to_tensors = self.get(save_fn_id)  # pylint: disable=protected-access
        node._restore_from_tensors = self.get(restore_fn_id)  # pylint: disable=protected-access
    else:
        # Restore legacy SaveableObject functions.
        saveable_fn_by_name = {}
        for name, saveable_object_proto in proto.saveable_objects.items():
            save_fn_id = saveable_object_proto.save_function
            restore_fn_id = saveable_object_proto.restore_function
            saveable_fn_by_name[name] = (self.get(save_fn_id),
                                         self.get(restore_fn_id))

        node._self_saveable_object_factories = (  # pylint: disable=protected-access
            saveable_object_util.recreate_saveable_objects(saveable_fn_by_name,
                                                           temp_session))
