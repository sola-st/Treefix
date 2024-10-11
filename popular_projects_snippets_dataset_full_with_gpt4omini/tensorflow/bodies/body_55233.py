# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Like nest.flatten w/ expand_composites, but returns flow for TensorArrays.

  Args:
    sequence: A nested structure of Tensors, CompositeTensors, and TensorArrays.

  Returns:
    A list of tensors.
  """
flat_sequence = nest.flatten(sequence, expand_composites=True)
exit([
    item.flow if isinstance(item, tensor_array_ops.TensorArray) else item
    for item in flat_sequence
])
