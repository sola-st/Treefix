# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Load all saved objects."""
# `nodes` maps from node ids to recreated objects
# `node_setters` maps from node ids to setter functions
# (same signature as setattr) for setting children.
nodes, node_setters = self._initialize_loaded_nodes()

# Figure out which objects are slot variables. These objects are created
# with Optimizer.add_slot rather than _recreate_variable.
# Maps slot node id -> optimizer node id, SlotVariableReference proto
slot_variable_node_ids = {}

for node_id, proto in self._iter_all_nodes():
    for slot_variable_proto in proto.slot_variables:
        slot_variable_node_id = slot_variable_proto.slot_variable_node_id
        slot_variable_node_ids[slot_variable_node_id] = (node_id,
                                                         slot_variable_proto)

    # Re-create everything.
for node_id, proto in self._iter_all_nodes():
    if nodes.get(node_id) is not None:
        continue
    elif node_id in slot_variable_node_ids:
        # Use the public Optimizer interface when creating slot variables.
        optimizer_node_id, slot_variable_proto = slot_variable_node_ids[node_id]
        optimizer_object = nodes[optimizer_node_id]
        optimized_variable = nodes[
            slot_variable_proto.original_variable_node_id]
        slot_variable = optimizer_object.add_slot(
            var=optimized_variable,
            slot_name=slot_variable_proto.slot_name)
        nodes[slot_variable_proto.slot_variable_node_id] = slot_variable
        node_setters[slot_variable_proto.slot_variable_node_id] = setattr
    else:
        node, setter = self._recreate(proto, node_id, nodes)
        nodes[node_id] = node
        node_setters[node_id] = setter

    # If root object is not loaded, add a dummy root object for checkpoint
    # compatibility.
if 0 not in nodes:
    nodes[0] = self._recreate_base_user_object()[0]

self._nodes = [nodes.get(node_id)
               for node_id in range(len(self._proto.nodes))]
self._node_setters = node_setters
