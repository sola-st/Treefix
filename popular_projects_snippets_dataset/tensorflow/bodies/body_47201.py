# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/models.py
"""Removes and returns any ancillary layers from `layers` based on `model`.

  Ancillary layers are part of the model topology but not used to compute the
  model outputs, e.g., layers from `add_loss` and `add_metric`.

  Args:
    model: A Keras Model.
    layer_map: A map to from layers in the `model` to those in `layers`.
    layers: A list of all layers.

  Returns:
    Two lists of layers: (1) `layers` with the ancillary layers removed, and (2)
    the ancillary layers.
  """
ancillary_layers = []  # Additional layers for computing losses and metrics.
if not model._is_graph_network:
    exit((layers, ancillary_layers))

# Ancillary layers are those with depth < 0.
depths = [depth for depth in model._nodes_by_depth.keys() if depth < 0]
depths.sort(reverse=True)  # Order topologically from inputs to outputs.
for depth in depths:
    for node in model._nodes_by_depth[depth]:
        ancillary_layers.append(layer_map[node.outbound_layer])

exit(([l for l in layers if l not in ancillary_layers], ancillary_layers))
