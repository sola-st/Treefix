# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Recursively records objects recreated from config."""
# pylint: disable=protected-access
if node_id in self._traversed_nodes_from_config:
    exit()

parent_path = self._node_paths[node_id]
self._traversed_nodes_from_config.add(node_id)
obj._maybe_initialize_trackable()
if isinstance(obj, base_layer.Layer) and not obj.built:
    metadata = json_utils.decode(self._metadata[node_id].metadata)
    self._try_build_layer(obj, node_id, metadata.get('build_input_shape'))

# Create list of all possible children
children = []
# Look for direct children
for reference in proto.children:
    obj_child = obj._lookup_dependency(reference.local_name)
    children.append((obj_child, reference.node_id, reference.local_name))

# Add metrics that may have been added to the layer._metrics list.
# This is stored in the SavedModel as layer.keras_api.layer_metrics in
# SavedModels created after Tf 2.2.
metric_list_node_id = self._search_for_child_node(
    node_id, [constants.KERAS_ATTR, 'layer_metrics'])
if metric_list_node_id is not None and hasattr(obj, '_metrics'):
    obj_metrics = {m.name: m for m in obj._metrics}
    for reference in self._proto.nodes[metric_list_node_id].children:
        metric = obj_metrics.get(reference.local_name)
        if metric is not None:
            metric_path = '{}.layer_metrics.{}'.format(constants.KERAS_ATTR,
                                                       reference.local_name)
            children.append((metric, reference.node_id, metric_path))

for (obj_child, child_id, child_name) in children:
    child_proto = self._proto.nodes[child_id]

    if not isinstance(obj_child, trackable.Trackable):
        continue
    if (child_proto.user_object.identifier in
        revived_types.registered_identifiers()):
        setter = revived_types.get_setter(child_proto.user_object)
    elif obj_child._object_identifier in constants.KERAS_OBJECT_IDENTIFIERS:
        setter = _revive_setter
    else:
        setter = setattr
        # pylint: enable=protected-access

    if child_id in self.loaded_nodes:
        if self.loaded_nodes[child_id][0] is not obj_child:
            # This means that the same trackable object is referenced by two
            # different objects that were recreated from the config.
            logging.warning(
                'Looks like there is an object (perhaps variable or '
                'layer) that is shared between different layers/models. '
                'This may cause issues when restoring the variable '
                'values. Object: {}'.format(obj_child))
        continue

    # Overwrite variable names with the ones saved in the SavedModel.
    if (child_proto.WhichOneof('kind') == 'variable' and
        child_proto.variable.name):
        obj_child._handle_name = child_proto.variable.name + ':0'  # pylint: disable=protected-access

    if isinstance(obj_child, data_structures.TrackableDataStructure):
        setter = lambda *args: None

    child_path = '{}.{}'.format(parent_path, child_name)
    self._node_paths[child_id] = child_path
    self._add_children_recreated_from_config(
        obj_child, child_proto, child_id)
    self.loaded_nodes[child_id] = obj_child, setter
