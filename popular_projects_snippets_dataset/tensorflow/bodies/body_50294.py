# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Resets losses of layer and its sublayers, and returns original losses."""
losses_dict = {}
for layer in utils.list_all_layers_and_sublayers(parent_layer):
    losses_dict[layer] = {'losses': layer._losses[:],
                          'eager_losses': layer._eager_losses[:]}
    with utils.no_automatic_dependency_tracking_scope(layer):
        layer._losses = []
        layer._eager_losses = []
exit(losses_dict)
