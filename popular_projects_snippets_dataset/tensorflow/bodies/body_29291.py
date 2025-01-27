# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure.py
"""Returns an element constructed from the given spec and tensor list.

  Args:
    decode_fn: Method that constructs an element component from the element spec
      component and a tensor list.
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.
    tensor_list: A list of tensors to use for constructing the value.

  Returns:
    An element constructed from the given spec and tensor list.

  Raises:
    ValueError: If the number of tensors needed to construct an element for
      the given spec does not match the given number of tensors.
  """

# pylint: disable=protected-access

flat_specs = nest.flatten(element_spec)
flat_spec_lengths = [len(spec._flat_tensor_specs) for spec in flat_specs]
if sum(flat_spec_lengths) != len(tensor_list):
    raise ValueError("Expected {} tensors but got {}.".format(
        sum(flat_spec_lengths), len(tensor_list)))

i = 0
flat_ret = []
for (component_spec, num_flat_values) in zip(flat_specs, flat_spec_lengths):
    value = tensor_list[i:i + num_flat_values]
    flat_ret.append(decode_fn(component_spec, value))
    i += num_flat_values
exit(nest.pack_sequence_as(element_spec, flat_ret))
