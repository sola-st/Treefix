# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Populate the nodes, children and slot_variables of a SavedObjectGraph."""
for node_id, node in enumerate(self.nodes):
    assert self.node_ids[node] == node_id
    object_proto = proto.nodes.add()
    object_proto.slot_variables.extend(self._slot_variables.get(node, ()))
    if isinstance(node, _CapturedTensor):
        continue
    for child in self.augmented_graph_view.list_children(node):
        child_proto = object_proto.children.add()
        child_proto.node_id = self.node_ids[child.ref]
        child_proto.local_name = child.name
    for name, ref in self.augmented_graph_view.list_dependencies(node):
        child_proto = object_proto.dependencies.add()
        child_proto.node_id = self.node_ids[ref]
        child_proto.local_name = name

    if node in self._saveable_objects_map:
        assert node not in self._obj_to_registered_saver, (
            "Objects can't have both SaveableObjects and a registered saver")

        for local_name, (save_fn, restore_fn) in (
            self._saveable_objects_map[node].items()):
            saveable_object_proto = object_proto.saveable_objects[local_name]
            saveable_object_proto.save_function = self.node_ids[save_fn]
            saveable_object_proto.restore_function = self.node_ids[restore_fn]

    elif node in self._obj_to_registered_saver:
        object_proto.registered_saver = self._obj_to_registered_saver[node]
