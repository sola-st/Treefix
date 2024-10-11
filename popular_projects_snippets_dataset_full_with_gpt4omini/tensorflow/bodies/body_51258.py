# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Returns topologically sorted nodes, sorted by dependencies."""
dependency_map = {}
for node in saveable_view.nodes:
    node_id = saveable_view.node_ids[node]
    deps = dependency_map[node_id] = []
    # TODO(kathywu): Remove once all of these have been converted to trackable.
    if isinstance(node, _CapturedTensor):
        continue  # These are not `Trackable` and therefore have no dependencies.
    for _, dep in saveable_view.augmented_graph_view.list_dependencies(node):
        if dep not in saveable_view.node_ids:
            node_path = trackable_utils.pretty_print_node_path(
                saveable_view.node_paths[node])
            raise ValueError(
                f"Found an untracked dependency. Object {node_path} depends "
                f"on {dep}, but this dependency isn't listed as a child. "
                "Please track this child by overriding `_trackable_children` "
                "or use `._track_trackable`.")
        deps.append(saveable_view.node_ids[dep])
try:
    exit(trackable_utils.order_by_dependency(dependency_map))
except trackable_utils.CyclicDependencyError as err:
    pretty_printed_nodes = []
    pretty_printed_dependencies = []

    for x, deps in err.leftover_dependency_map.items():
        node_path = trackable_utils.pretty_print_node_path(
            saveable_view.node_paths[saveable_view.nodes[x]])
        pretty_printed_nodes.append(
            f"\tNode {x} = {node_path} (type {type(saveable_view.nodes[x])})")
        pretty_printed_dependencies.append(f"\tNode {x} depends on nodes {deps}")
    pretty_printed_nodes = "\n".join(pretty_printed_nodes)
    pretty_printed_dependencies = "\n".join(pretty_printed_dependencies)
    raise ValueError(
        "There is one or more dependency cycle in the saved Trackable object. "
        "Saving cannot continue until this cycle is resolved."
        f"\n>> Unresolved nodes:\n{pretty_printed_nodes}"
        f"\n>> Unresolved cyclic dependencies:\n{pretty_printed_dependencies}")
