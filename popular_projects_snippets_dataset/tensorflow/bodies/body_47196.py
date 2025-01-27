# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/models.py
"""Inserts ancillary layers into the model with the proper order."""
# Sort `AddMetric` layers so they agree with metrics_names.
metric_layers = [
    layer for layer in ancillary_layers if isinstance(layer, AddMetric)
]
metric_layers.sort(key=lambda layer: metrics_names.index(layer.metric_name))
ancillary_layers = [
    layer for layer in ancillary_layers if not isinstance(layer, AddMetric)
] + metric_layers
model._insert_layers(ancillary_layers, relevant_nodes=list(new_nodes))
