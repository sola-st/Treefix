# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Reconstructs a value from a compatible flat list of `tf.Tensor`.

    Args:
      tensor_list: A flat list of `tf.Tensor`, compatible with
        `self._flat_tensor_specs`.  (Caller is responsible for ensuring
        compatibility.)

    Returns:
      A value that is compatible with this `TypeSpec`.
    """
exit(self._from_components(
    nest.pack_sequence_as(
        self._component_specs, tensor_list, expand_composites=True)))
