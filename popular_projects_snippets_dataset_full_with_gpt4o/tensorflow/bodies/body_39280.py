# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Queues the restoration of trackable's children or defers them."""
# pylint: disable=protected-access
trackable = checkpoint_position.trackable
for child in checkpoint_position.object_proto.children:
    child_position = checkpoint_position.create_child_position(child.node_id)
    local_object = trackable._lookup_dependency(child.local_name)
    child_proto = child_position.object_proto
    if local_object is None:
        # We don't yet have a dependency registered with this name. Save it
        # in case we do.
        if child_proto.HasField("has_checkpoint_values"):
            has_value = child_proto.has_checkpoint_values.value
        else:
            # If the field is not set, do a simple check to see if the dependency
            # has children and/or checkpointed values.
            has_value = bool(
                child_proto.children or child_proto.attributes or
                child_proto.slot_variables or
                child_proto.HasField("registered_saver"))
        if has_value:
            trackable._deferred_dependencies.setdefault(child.local_name,
                                                        []).append(child_position)
    else:
        if child_position.bind_object(trackable=local_object):
            # This object's correspondence is new, so dependencies need to be
            # visited. Delay doing it so that we get a breadth-first dependency
            # resolution order (shallowest paths first). The caller is responsible
            # for emptying visit_queue.
            visit_queue.append((child_position, local_object))
