# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Restores nodes from a dict.

  Requires that the `Trackable` Python object has been bound to an object
  ID in the checkpoint.

  Args:
    save_path: a string represents path to the checkpoint.
    nodes_to_restore: a dict maps `node_id` to `trackable` to be restored.
  """
if save_path is None:
    raise ValueError("save_path cannot be empty.")
if not isinstance(nodes_to_restore, dict):
    raise ValueError(
        "Expecting a dictionary of node_id to Trackable for nodes_to_restore.")

# pylint:disable=g-import-not-at-top
# There are circular dependencies between Trackable and SaveableObject,
# so we must import it here.
from tensorflow.python.training.saving import saveable_object_util
# pylint:enable=g-import-not-at-top

ckpt_view = checkpoint_view.CheckpointView(save_path)
ckpt_view_descendants = ckpt_view.descendants()
for node_id, trackable in nodes_to_restore.items():
    # node_id does not have a corresponding Checkpoint value.
    if (node_id not in ckpt_view_descendants or
        ckpt_view._object_graph_proto.nodes[  # pylint: disable=protected-access
            node_id] is None):
        raise ValueError(
            f"The expected node_id: {node_id} to Trackable {trackable} to "
            "restore does not exist in the checkpoint.")
    # Trackable mapped to node_id to restore is empty.
    if trackable is None or not isinstance(trackable, base.Trackable):
        raise ValueError(
            f"Expecting a valid Trackable to node_id: {node_id} but got "
            f"trackable: {trackable}."
        )

serialized_tensors = object_identity.ObjectIdentityDictionary()
for node_id, current_trackable in nodes_to_restore.items():
    ckpt_contains_serialized_tensors = ckpt_view._object_graph_proto.nodes[  # pylint: disable=protected-access
        node_id].attributes
    node = ckpt_view._object_graph_proto.nodes[node_id]  # pylint: disable=protected-access
    trackable_has_serialize_to_tensor = saveable_object_util.trackable_has_serialize_to_tensor(
        current_trackable)
    if not trackable_has_serialize_to_tensor:
        if not node.attributes:
            if current_trackable._gather_saveables_for_checkpoint():  # pylint: disable=protected-access
                raise ValueError(
                    f"Trackable {current_trackable} expects checkpointed values but "
                    "checkpoint does not contain serialized tensors for node_id: "
                    f"{node_id}.")
            else:
                continue
        object_names = object_identity.ObjectIdentityDictionary()
        object_names[current_trackable] = trackable_utils.extract_object_name(
            node.attributes[0].checkpoint_key)
        checkpoint_factory_map, _ = save_util_v1.get_checkpoint_factories_and_keys(
            object_names, None)
        saveable_objects = save_util_v1.generate_saveable_objects(
            checkpoint_factory_map)[0]
        if len(node.attributes) != len(saveable_objects):
            raise ValueError("Size for saveable_objects for Trackable: "
                             f"{len(saveable_objects)} did not match the size for "
                             "serialized_tensors for checkpoint: "
                             f"{len(node.attributes)}.")
        current_trackable = saveable_object_util.SaveableCompatibilityConverter(
            current_trackable, saveable_objects)

    serialized_tensors[
        current_trackable] = current_trackable._serialize_to_tensors()  # pylint: disable=protected-access
    trackable_expects_ckpted_value = bool(serialized_tensors[current_trackable])

    if trackable_expects_ckpted_value and not ckpt_contains_serialized_tensors:
        raise ValueError(
            f"Trackable {current_trackable} expects checkpointed values but "
            "checkpoint does not contain serialized tensors for node_id: "
            f"{node_id}.")

    if not trackable_expects_ckpted_value and ckpt_contains_serialized_tensors:
        raise ValueError(
            f"Trackable {current_trackable} does not expect checkpointed "
            "values but checkpoint contains serialized tensors: "
            f"{ckpt_contains_serialized_tensors} for node_id: {node_id}.")

    if len(node.attributes) != len(serialized_tensors[current_trackable]):
        raise ValueError("Size for serialized_tensors for Trackable: "
                         f"{len(serialized_tensors[current_trackable])} did not "
                         "match size for serialized_tensors for checkpoint: "
                         f"{len(node.attributes)}.")

    if not trackable_has_serialize_to_tensor:
        functional_saver.MultiDeviceSaver(serialized_tensors).restore(save_path)
    else:
        # Converts attribute.name to attribute.checkpoint_key since that's what
        # restore method is expecting. i.e., converts "a" to "/.ATTRIBUTES/a".
        serialized_tensors_renamed = object_identity.ObjectIdentityDictionary()
        serialized_tensors_renamed[current_trackable] = {}
        for attribute in node.attributes:
            name = attribute.name
            checkpoint_key = attribute.checkpoint_key
            serialized_tensors_renamed[current_trackable][
                checkpoint_key] = serialized_tensors[current_trackable][name]
        functional_saver.MultiDeviceSaver(serialized_tensors_renamed).restore(
            save_path)
