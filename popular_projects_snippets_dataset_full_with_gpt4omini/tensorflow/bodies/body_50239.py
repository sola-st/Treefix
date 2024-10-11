# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Finish setting up Keras objects.

    This function is executed after all objects and functions have been created.
    Call functions and losses are attached to each layer, and once all layers
    have been fully set up, graph networks are initialized.

    Subclassed models that are revived from the SavedModel are treated like
    layers, and have their call/loss functions attached here.
    """
# Finish setting up layers and subclassed models. This step attaches call
# functions and losses to each object, and sets model inputs/outputs.
layers_revived_from_config = []
layers_revived_from_saved_model = []
for node_id, (node, _) in self.loaded_nodes.items():
    if (not isinstance(node, base_layer.Layer) or
        # Don't finalize models until all layers have finished loading.
        node_id in self.model_layer_dependencies):
        continue

    self._unblock_model_reconstruction(node_id, node)

    if isinstance(node, input_layer.InputLayer):
        continue
    elif isinstance(node, metrics.Metric):
        continue

    if isinstance(node, (RevivedLayer, RevivedInputLayer)):
        layers_revived_from_saved_model.append(node)
    else:
        layers_revived_from_config.append(node)

_finalize_saved_model_layers(layers_revived_from_saved_model)
_finalize_config_layers(layers_revived_from_config)

# Initialize graph networks, now that layer dependencies have been resolved.
self._reconstruct_all_models()
