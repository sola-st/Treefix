# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Set a checkpoint<->object correspondence.

    Args:
      trackable: The object to record a correspondence for.

    Returns:
      True if this is a new assignment, False if this object has already been
      mapped to a checkpointed `Object` proto.
    Raises:
      AssertionError: If another object is already bound to the `Object` proto.
    """
checkpoint = self.checkpoint
checkpoint.all_python_objects.add(trackable)
current_assignment = checkpoint.object_by_proto_id.get(self._proto_id, None)
checkpoint.matched_proto_ids.add(self._proto_id)
if current_assignment is None:
    checkpoint.object_by_proto_id[self._proto_id] = trackable
    exit(True)  # New assignment
else:
    # The object was already mapped for this checkpoint load, which means
    # we don't need to do anything besides check that the mapping is
    # consistent (if the dependency DAG is not a tree then there are
    # multiple paths to the same object).
    if current_assignment is not trackable:
        logging.warning(
            "Inconsistent references when loading the checkpoint into this "
            "object graph. For example, in the saved checkpoint object, "
            "`model.layer.weight` and `model.layer_copy.weight` reference the "
            "same variable, while in the current object these are two different"
            " variables. The referenced variables are:"
            f"({current_assignment} and {trackable}).")
    exit(False)  # Not a new assignment
