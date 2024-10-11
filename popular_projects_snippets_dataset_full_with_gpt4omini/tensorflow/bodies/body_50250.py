# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Runs the final steps of loading Keras Layers from config."""
for layer in layers:
    # It is assumed that layers define their unconditional losses after being
    # recreated from the config and built. The exceptions to this
    # are Functional and Sequential models, which only store conditional losses
    # (losses dependent on the inputs) in the config. Unconditional losses like
    # weight regularization must be revived from the SavedModel.
    if _is_graph_network(layer):
        _restore_layer_unconditional_losses(layer)

    # Some layers, like Dense, record their activation loss function in the
    # config. However, not all layers do this, so the activation loss may be
    # missing when restored from the config/hdf5.
    # TODO(kathywu): Investigate ways to improve the config to ensure consistent
    # loading behavior between HDF5 and SavedModel.
    _restore_layer_activation_loss(layer)

    # Restore metrics list.
    _restore_layer_metrics(layer)

    # Restore RNN layer states.
    if (isinstance(layer, recurrent.RNN) and
        layer.stateful and
        hasattr(_get_keras_attr(layer), 'states')):
        layer.states = getattr(_get_keras_attr(layer), 'states', None)
        for variable in nest.flatten(layer.states):
            backend.track_variable(variable)

    # Perform any layer defined finalization of the layer state.
    layer.finalize_state()
