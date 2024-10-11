# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Queues slot variables for restoration."""
trackable = checkpoint_position.trackable
checkpoint = checkpoint_position.checkpoint
for deferred_slot_restoration in (checkpoint.deferred_slot_restorations.pop(
    checkpoint_position.proto_id, ())):
    slot_variable_position, slot_variable = (
        checkpoint_position.create_slot_variable_position(
            trackable, deferred_slot_restoration.original_variable,
            deferred_slot_restoration.slot_variable_id,
            deferred_slot_restoration.slot_name))
    if slot_variable_position is not None:
        visit_queue.append((slot_variable_position, slot_variable))
for slot_restoration in checkpoint.slot_restorations.pop(
    checkpoint_position.proto_id, ()):
    optimizer_object = checkpoint.object_by_proto_id.get(
        slot_restoration.optimizer_id, None)
    if optimizer_object is None:
        # The optimizer has not yet been created or tracked. Record in the
        # checkpoint that the slot variables need to be restored when it is.
        checkpoint.deferred_slot_restorations.setdefault(
            slot_restoration.optimizer_id, []).append(
                _DeferredSlotVariableRestoration(
                    original_variable=trackable,
                    slot_variable_id=slot_restoration.slot_variable_id,
                    slot_name=slot_restoration.slot_name))

    # `optimizer_object` can be a `Checkpoint` when user only needs the
    # attributes the optimizer holds, such as `iterations`. In those cases,
    # it would not have the optimizer's `_create_or_restore_slot_variable`
    # method.
    elif hasattr(optimizer_object, "_create_or_restore_slot_variable"):
        slot_variable_position, slot_variable = (
            checkpoint_position.create_slot_variable_position(
                optimizer_object, trackable, slot_restoration.slot_variable_id,
                slot_restoration.slot_name))
        if slot_variable_position is not None:
            visit_queue.append((slot_variable_position, slot_variable))
