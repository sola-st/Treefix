# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Reconstructs a value from a nested structure of Tensor/CompositeTensor.

    Args:
      components: A nested structure of `tf.Tensor` or `tf.CompositeTensor`,
        compatible with `self._component_specs`.  (Caller is responsible for
        ensuring compatibility.)

    Returns:
      A value that is compatible with this `TypeSpec`.
    """
# === Subclassing ===
# This method must be inexpensive (do not call TF ops).
raise NotImplementedError("%s._from_components()" % type(self).__name__)
