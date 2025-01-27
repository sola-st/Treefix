# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util_v1.py
"""Create SaveableObjects and corresponding SerializedTensor protos."""
named_saveable_objects = []
if saveables_cache is None:
    # No SaveableObject caching. Either we're executing eagerly, or building a
    # static save which is specialized to the current Python state.
    feed_additions = None
else:
    # If we are caching SaveableObjects, we need to build up a feed_dict with
    # functions computing volatile Python state to be saved with the
    # checkpoint.
    feed_additions = {}
for trackable, factory_data_list in checkpoint_factory_map.items():
    fill_object_proto = object_graph_proto is not None and node_ids is not None
    if fill_object_proto:
        object_proto = object_graph_proto.nodes[node_ids[trackable]]
    object_to_save = util.get_mapped_trackable(trackable, object_map)
    if saveables_cache is not None:
        cached_attributes = saveables_cache.setdefault(object_to_save, {})
    else:
        cached_attributes = None

    for factory_data in factory_data_list:
        name = factory_data.name
        key = factory_data.checkpoint_key
        saveable_factory = factory_data.factory

        # See if we can skip saving this checkpoint key.
        saveables = cached_attributes.get(name) if cached_attributes else None
        if saveables is not None:
            for saveable in saveables:
                if key not in saveable.name:
                    # The checkpoint key for this SaveableObject is different. We
                    # need to re-create it.
                    saveables = None
                    del cached_attributes[name]
                    break

        if saveables is None:
            if callable(saveable_factory):
                maybe_saveable = saveable_object_util.create_saveable_object(
                    name, key, saveable_factory, call_with_mapped_captures)
            else:
                maybe_saveable = saveable_factory
            if isinstance(maybe_saveable, saveable_object_lib.SaveableObject):
                saveables = (maybe_saveable,)
            else:
                saveables = tuple(
                    saveable_object_util.saveable_objects_for_op(
                        op=maybe_saveable, name=key))
            for saveable in saveables:
                if key not in saveable.name:
                    raise AssertionError(
                        f"The object {trackable} produced a SaveableObject with name "
                        f"'{saveable.name}' for attribute '{name}'. Expected a name"
                        f" containing '{key}'.")
            if cached_attributes is not None:
                cached_attributes[name] = saveables

        if isinstance(object_to_save, python_state.PythonState):
            assert len(saveables) == 1
            saveable = saveables[0]

            if feed_additions is None:
                assert saveables_cache is None
                # If we're not caching saveables, then we're either executing
                # eagerly or building a static save/restore (e.g. for a
                # SavedModel). In either case, we should embed the current Python
                # state in the graph rather than relying on a feed dict.
                saveables = (saveable.freeze(),)
            else:
                feed_additions.update(saveable.feed_dict_additions())
        named_saveable_objects.extend(saveables)

        # Update the object proto.
        # For updated Trackables that override serialize_to_tensors, add an
        # attribute for each tensor that is serialized.
        # For Trackables that have SaveableObjects or a legacy saveable name,
        # add a single attribute to the proto.
        if not fill_object_proto:
            continue
        if (isinstance(saveables[0], saveable_object_util.TrackableSaveable) and
            (saveable_compat.force_checkpoint_conversion_enabled() or
             saveable_compat.get_saveable_name(object_to_save) is None)):
            for local_name, local_key in (
                saveables[0].get_proto_names_and_checkpoint_keys()):
                object_proto.attributes.add(
                    name=local_name,
                    checkpoint_key=local_key,
                    full_name=util.get_full_name(object_to_save))
        else:
            object_proto.attributes.add(
                name=name,
                checkpoint_key=key,
                full_name=util.get_full_name(object_to_save))

exit((named_saveable_objects, feed_additions))
