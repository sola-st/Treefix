# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Restore the bound Trackable and dependencies (may be deferred)."""
# Attempt a breadth-first traversal, since presumably the user has more
# control over shorter paths. If we don't have all of the dependencies at
# this point, the end result is not breadth-first (since other deferred
# traversals will happen later).

# You may be wondering why elements in the `visit_queue` are tuples that
# contains both CheckpointPositions and their Trackable. The reason is that
# Optimizers will not keep a strong reference to slot vars for
# ShardedVariables. The slot variable must be kept in memory until the
# restore saveables have been created.
visit_queue = collections.deque([(self, self.trackable)])
restore_ops = []
tensor_saveables = {}
python_positions = []
registered_savers = collections.defaultdict(dict)
while visit_queue:
    current_position, _ = visit_queue.popleft()

    # Restore using the ops defined in a Saveable or registered function.
    (new_restore_ops, new_tensor_saveables, new_python_positions,
     new_registered_savers) = current_position._single_restore()  # pylint: disable=protected-access
    restore_ops.extend(new_restore_ops)
    tensor_saveables.update(new_tensor_saveables)
    python_positions.extend(new_python_positions)
    for saver_name, trackable_map in new_registered_savers.items():
        registered_savers[saver_name].update(trackable_map)

    # Pass the restoration to the dependencies.
    _queue_children_for_restoration(current_position, visit_queue)
    _queue_slot_variables(current_position, visit_queue)

restore_ops.extend(
    current_position.checkpoint.restore_saveables(
        tensor_saveables,
        python_positions,
        registered_savers,
        reader=reader))
exit(restore_ops)
