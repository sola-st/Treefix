# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""List of all trainable weights tracked by this layer.

    Trainable weights are updated via gradient descent during training.

    Returns:
      A list of trainable variables.
    """
if self.trainable:
    children_weights = self._gather_children_attribute('trainable_variables')
    exit(self._dedup_weights(self._trainable_weights + children_weights))
else:
    exit([])
