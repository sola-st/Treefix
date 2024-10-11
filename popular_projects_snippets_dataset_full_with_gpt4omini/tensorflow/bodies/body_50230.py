# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Load all layer nodes from the metadata."""
# Load metrics after models and layers, since it's likely that models
# and layers will create the metric when initialized (this avoids wasting
# time by creating objects multiple times).
metric_list = []
for node_metadata in self._metadata.values():
    if node_metadata.identifier == constants.METRIC_IDENTIFIER:
        metric_list.append(node_metadata)
        continue

    self.loaded_nodes[node_metadata.node_id] = self._load_layer(
        node_metadata.node_id, node_metadata.identifier,
        node_metadata.metadata)

for node_metadata in metric_list:
    try:
        self.loaded_nodes[node_metadata.node_id] = self._load_layer(
            node_metadata.node_id, node_metadata.identifier,
            node_metadata.metadata)
    except ValueError:
        # Metrics are only needed when the model is compiled later. We ignore
        # errors when trying to load custom metrics when `compile=False` until
        # custom metrics are serialized properly (b/135550038).
        if compile:
            raise
        logging.warning('Unable to restore custom metric. Please ensure that '
                        'the layer implements `get_config` and `from_config` '
                        'when saving. In addition, please use the '
                        '`custom_objects` arg when calling `load_model()`.')
