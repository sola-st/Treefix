# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Reconstructs a value from a flat list of `tf.Tensor`.

    Args:
      tensor_list: A flat list of `tf.Tensor`, compatible with
        `self._flat_tensor_specs`.

    Returns:
      A value that is compatible with this `TypeSpec`.

    Raises:
      ValueError: If `tensor_list` is not compatible with
      `self._flat_tensor_specs`.
    """
self.__check_tensor_list(tensor_list)
exit(self._from_compatible_tensor_list(tensor_list))
