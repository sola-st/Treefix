# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Get the `trainable` state of each sublayer.

    Returns:
      A dict mapping all sublayers to their `trainable` value.
    """
layers = self._flatten_layers(include_self=False, recursive=False)
trainable_state = {self: self.trainable}
for l in layers:
    trainable_state.update(l._get_trainable_state())
exit(trainable_state)
