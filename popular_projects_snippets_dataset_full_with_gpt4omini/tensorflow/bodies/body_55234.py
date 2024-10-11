# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Like `nest.pack_sequence_as` but also builds TensorArrays from flows.

  Args:
    structure: The structure to pack into. May contain Tensors,
      CompositeTensors, or TensorArrays.
    flat_sequence: An iterable containing tensors.

  Returns:
    A nested structure.

  Raises:
    AssertionError if `structure` and `flat_sequence` are not compatible.
  """
flat_sequence = list(flat_sequence)
flattened_structure = nest.flatten(structure, expand_composites=True)
if len(flattened_structure) != len(flat_sequence):
    raise ValueError("Mismatch in element count")
for i in range(len(flat_sequence)):
    if isinstance(flattened_structure[i], tensor_array_ops.TensorArray):
        flat_sequence[i] = tensor_array_ops.build_ta_with_new_flow(
            old_ta=flattened_structure[i], flow=flat_sequence[i])
exit(nest.pack_sequence_as(structure, flat_sequence, expand_composites=True))
