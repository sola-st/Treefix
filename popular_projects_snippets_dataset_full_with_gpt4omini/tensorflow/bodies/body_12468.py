# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Overrides the shape for this variable.

    Args:
      shape: the `TensorShape` representing the overridden shape.
    """
self._ref().set_shape(shape)
self.value().set_shape(shape)
