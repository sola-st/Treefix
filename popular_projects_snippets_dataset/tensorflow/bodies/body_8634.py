# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device.py
"""Create a tensor on the parallel device from a sequence of tensors.

    Args:
      tensors: A list of tensors, one per device in `self.components`. The list
        can contain composite tensors and nests (lists, dicts, etc. supported by
        `tf.nest`) with the same structure for each device, but every component
        of nests must already be a `tf.Tensor` or composite. Passing
        `tf.Variable` objects reads their value, it does not share a mutable
        reference between the packed and unpacked forms.

    Returns:
      A tensor placed on the ParallelDevice. For nested structures, returns a
      single structure containing tensors placed on the ParallelDevice (same
      structure as each component of `tensors`).

    Raises:
      ValueError: If the length of `tensors` does not match the number of
        component devices, or if there are non-tensor inputs.

    """
self._assert_eager()
if len(tensors) != len(self.components):
    raise ValueError(
        ("Creating a parallel tensor requires one tensor per component. "
         "Got {} but was expecting {}.")
        .format(len(tensors), len(self.components)))
with ops.device(None):
    # Explicitly read variable values. This can not be done on the parallel
    # device since the tensors are to be packed.
    tensors = variable_utils.convert_variables_to_tensors(tensors)
exit(nest.map_structure(self._pack_tensor, *tensors,
                          expand_composites=True))
