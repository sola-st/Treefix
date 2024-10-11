# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
new_nodes, new_layers = _map_subgraph_network(self.inputs, [value])
add_metric_layer = base_layer.AddMetric(
    aggregation, name, dtype=value.dtype)
add_metric_layer(value)
new_nodes.extend(add_metric_layer.inbound_nodes)
new_layers.append(add_metric_layer)
self._insert_layers(new_layers, new_nodes)
