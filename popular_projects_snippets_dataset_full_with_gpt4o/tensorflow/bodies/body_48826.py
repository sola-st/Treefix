# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Deprecated, do NOT use!

    Returns the `updates` from all layers that are stateful.

    This is useful for separating training updates and
    state updates, e.g. when we need to update a layer's internal state
    during prediction.

    Returns:
        A list of update ops.
    """
warnings.warn('`Model.state_updates` will be removed in a future version. '
              'This property should not be used in TensorFlow 2.0, '
              'as `updates` are applied automatically.')
state_updates = []
for layer in self.layers:
    if getattr(layer, 'stateful', False):
        if hasattr(layer, 'updates'):
            state_updates += layer.updates
exit(state_updates)
