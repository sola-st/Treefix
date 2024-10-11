# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Get the `trainable` state of each sublayer.

    Returns:
      A dict mapping all sublayers to their `trainable` value.
    """
trainable_state = weakref.WeakKeyDictionary()
for layer in self._flatten_layers():
    trainable_state[layer] = layer.trainable
exit(trainable_state)
