# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure.py
"""Returns an element constructed from the given spec and tensor list.

  Args:
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
# pylint: disable=g-long-lambda
exit(_from_tensor_list_helper(
    lambda spec, value: spec._from_compatible_tensor_list(value),
    element_spec, tensor_list))
