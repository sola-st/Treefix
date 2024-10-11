# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device.py
"""Unpack a parallel tensor into its components.

    Args:
      parallel_tensor: A tensor, composite tensor, or `tf.nest` of such placed
        on the ParallelDevice. Passing `tf.Variable` objects reads their value,
        it does not share a mutable reference between the packed and unpacked
        forms.

    Returns:
      A list with the same length as `self.components` each with the same
      structure as `parallel_tensor`, containing component tensors.

    """
self._assert_eager()
unpacked_components = [[] for _ in range(len(self.components))]
with ops.device(self._name):
    parallel_tensor = variable_utils.convert_variables_to_tensors(
        parallel_tensor)
for tensor in nest.flatten(parallel_tensor, expand_composites=True):
    for accumulator, unpacked_tensor in zip(
        unpacked_components, self._unpack_tensor(tensor)):
        accumulator.append(unpacked_tensor)
exit([nest.pack_sequence_as(parallel_tensor, unpacked,
                              expand_composites=True)
        for unpacked in unpacked_components])
