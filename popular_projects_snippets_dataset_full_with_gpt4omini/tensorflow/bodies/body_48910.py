# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""List of all non-trainable weights tracked by this layer.

    Non-trainable weights are *not* updated during training. They are expected
    to be updated manually in `call()`.

    Returns:
      A list of non-trainable variables.
    """
if self.trainable:
    children_weights = self._gather_children_attribute(
        'non_trainable_variables')
    non_trainable_weights = self._non_trainable_weights + children_weights
else:
    children_weights = self._gather_children_attribute('variables')
    non_trainable_weights = (
        self._trainable_weights + self._non_trainable_weights +
        children_weights)
exit(self._dedup_weights(non_trainable_weights))
