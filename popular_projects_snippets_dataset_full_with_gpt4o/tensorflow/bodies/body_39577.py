# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/util.py
"""Determines which objects have checkpoint values and save this to the proto.

  Args:
    object_graph_proto: A `TrackableObjectGraph` proto.
  """
# Trackable -> set of all trackables that depend on it (the "parents").
# If a trackable has checkpoint values, then all of the parents can be
# marked as having checkpoint values.
parents = {}
checkpointed_trackables = object_identity.ObjectIdentitySet()

# First pass: build dictionary of parent objects and initial set of
# checkpointed trackables.
checkpointed_trackables = set()
for node_id, object_proto in enumerate(object_graph_proto.nodes):
    if (object_proto.attributes or object_proto.slot_variables or
        object_proto.HasField("registered_saver")):
        checkpointed_trackables.add(node_id)
    for child_proto in object_proto.children:
        child = child_proto.node_id
        if child not in parents:
            parents[child] = set()
        parents[child].add(node_id)

  # Second pass: add all connected parents to set of checkpointed trackables.
to_visit = set()
to_visit.update(checkpointed_trackables)

while to_visit:
    trackable = to_visit.pop()
    if trackable not in parents:
        # Some trackables may not have parents (e.g. slot variables).
        continue
    current_parents = parents.pop(trackable)
    checkpointed_trackables.update(current_parents)
    for parent in current_parents:
        if parent in parents:
            to_visit.add(parent)

for node_id, object_proto in enumerate(object_graph_proto.nodes):
    object_proto.has_checkpoint_values.value = bool(
        node_id in checkpointed_trackables)
