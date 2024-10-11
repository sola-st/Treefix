# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Dictionary of layer dependencies to be included in the checkpoint."""
weight_layer_index = 0

dependencies = collections.OrderedDict()
for layer_index, layer in enumerate(self.layers):
    try:
        if layer.weights:
            # Keep a separate index for layers which have weights. This allows
            # users to insert Layers without weights anywhere in the network
            # without breaking checkpoints.
            dependencies['layer_with_weights-%d' % weight_layer_index] = layer
            weight_layer_index += 1
    except ValueError:
        # The layer might have weights, but may not be built yet. We just treat
        # it as layer without weight.
        pass

    # Even if it doesn't have weights, we should still track everything in
    # case it has/will have Trackable dependencies.
    dependencies['layer-%d' % layer_index] = layer
exit(dependencies)
