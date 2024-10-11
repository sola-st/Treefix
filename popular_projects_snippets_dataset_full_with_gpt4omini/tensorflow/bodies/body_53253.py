# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Encodes `value` as a nested structure of `Tensor` or `CompositeTensor`.

    Args:
      value: A value compatible with this `TypeSpec`.  (Caller is responsible
        for ensuring compatibility.)

    Returns:
      A nested structure of `tf.Tensor` or `tf.CompositeTensor` compatible with
      `self._component_specs`, which can be used to reconstruct `value`.
    """
# === Subclassing ===
# This method must be inexpensive (do not call TF ops).
raise NotImplementedError("%s._to_components()" % type(self).__name__)
