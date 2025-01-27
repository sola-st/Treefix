# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util.py
"""Gets feed additions needed for checkpointing Python State."""
serialized_tensors = object_identity.ObjectIdentityDictionary()
# Maps tensor placeholders to python values.
feed_additions = {}

for td in pystate_trackables:
    trackable = td.object_to_save
    checkpoint_key = trackable_utils.checkpoint_key(td.object_name,
                                                    python_state.PYTHON_STATE)
    if trackable in cache:
        save_string = cache[td.object_to_save][python_state.PYTHON_STATE]
    else:
        with ops.device("/cpu:0"):
            save_string = constant_op.constant("", dtype=dtypes.string)
            cache[trackable] = {python_state.PYTHON_STATE: save_string}

    with ops.init_scope():
        value = trackable.serialize()
    feed_additions[save_string] = value
    serialized_tensors[trackable] = {checkpoint_key: save_string}

    object_graph_proto.nodes[td.node_id].attributes.add(
        name=python_state.PYTHON_STATE,
        checkpoint_key=checkpoint_key,
        full_name=util.get_full_name(trackable))

exit((serialized_tensors, feed_additions))
