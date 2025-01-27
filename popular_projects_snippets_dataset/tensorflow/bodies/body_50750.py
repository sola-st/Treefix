# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Orders the node ids so that dependencies appear first."""
if self._filtered_nodes is None:
    unordered_ids = range(len(self._proto.nodes))
else:
    unordered_ids = list(self._filtered_nodes)

# Maps node ids -> list of dependencies (ids of other nodes that must be
# loaded before it).
dependency_map = collections.defaultdict(list)
for node_id in unordered_ids:
    deps = dependency_map[node_id]
    if self._loaded_nodes.get(node_id) is not None:
        # Deps are only used if the node has not been created.
        continue
    proto = self._proto.nodes[node_id]
    for dep in set(self._get_node_dependencies(proto).values()):
        deps.append(dep)
        if self._filtered_nodes is not None and dep not in self._filtered_nodes:
            raise ValueError(
                "Unable to partially load SavedModel since the specified filter "
                "does not include all required objects for loading (e.g. "
                "variables used in functions or deserialization dependencies). "
                "Please include this path in the filter: "
                f"{self._pretty_printer.node_names[dep]}")

      # Add optimizer slot variable to dependency map.
    prev_slot = None
    for slot_variable_proto in proto.slot_variables:
        slot_variable_node_id = slot_variable_proto.slot_variable_node_id
        # The optimizer and original variable must be created before the slot
        # variable, since the slot variable is generated using the Optimizer's
        # add_slot API.
        slot_deps = dependency_map[slot_variable_node_id]
        slot_deps.append(node_id)
        slot_deps.append(slot_variable_proto.original_variable_node_id)

        if prev_slot is not None:
            # Add previous slot to deps so that the optimizer slot variables are
            # added in order. The ordering is needed because the slot name and
            # variable are both added to ordered lists, which are exposed to the
            # user via `Optimizer.get_slot_names()` and `Optimizer.weights`.
            # TODO(kathywu): Maybe enforce some sort of deterministic ordering in
            # `order_by_dependency` to avoid doing this?
            slot_deps.append(prev_slot)
        prev_slot = slot_variable_node_id
try:
    exit(list(trackable_utils.order_by_dependency(dependency_map)))
except trackable_utils.CyclicDependencyError:
    # This should not happen since there is already a validation for cycles
    # when saving, but raise an error just in case.
    raise ValueError("Encountered a cycle in the deserialization dependencies"
                     "in the SavedModel. This is extremely unexpected, please"
                     "file a bug and make sure you are not manually modifying"
                     " the SavedModel.")
