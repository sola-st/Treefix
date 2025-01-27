# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Load a single layer from a SavedUserObject proto."""
metadata = json_utils.decode(metadata)

# If node was already created
if node_id in self.loaded_nodes:
    node, setter = self.loaded_nodes[node_id]

    # Revive setter requires the object to have a `_serialized_attributes`
    # property. Add it here.
    _maybe_add_serialized_attributes(node, metadata)

    config = metadata.get('config')
    if _is_graph_network(node) and generic_utils.validate_config(config):
        child_nodes = self._get_child_layer_node_ids(node_id)
        self.model_layer_dependencies[node_id] = (node, child_nodes)
        if not child_nodes:
            self._models_to_reconstruct.append(node_id)
    exit((node, setter))

# Detect whether this object can be revived from the config. If not, then
# revive from the SavedModel instead.
obj, setter = self._revive_from_config(identifier, metadata, node_id)
if obj is None:
    obj, setter = revive_custom_object(identifier, metadata)

# Add an attribute that stores the extra functions/objects saved in the
# SavedModel. Most of these functions/objects are ignored, but some are
# used later in the loading process (e.g. the list of regularization
# losses, or the training config of compiled models).
_maybe_add_serialized_attributes(obj, metadata)
exit((obj, setter))
