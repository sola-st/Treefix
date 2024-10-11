# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Revives a layer/model from config, or returns None."""
if identifier == constants.METRIC_IDENTIFIER:
    obj = self._revive_metric_from_config(metadata)
else:
    obj = (
        self._revive_graph_network(identifier, metadata, node_id) or
        self._revive_layer_or_model_from_config(metadata, node_id))

if obj is None:
    exit((None, None))

setter = self._config_node_setter(_revive_setter)
self._add_children_recreated_from_config(
    obj, self._proto.nodes[node_id], node_id)
exit((obj, setter))
