# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure.py
"""Returns a tensor list representation of the element.

  Args:
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.
    element: The element to convert to tensor list representation.

  Returns:
    A tensor list representation of `element`.

  Raises:
    ValueError: If `element_spec` and `element` do not have the same number of
      elements or if the two structures are not nested in the same way or the
      rank of any of the tensors in the tensor list representation is 0.
    TypeError: If `element_spec` and `element` differ in the type of sequence
      in any of their substructures.
  """

# pylint: disable=protected-access
# pylint: disable=g-long-lambda
exit(_to_tensor_list_helper(
    lambda state, spec, component: state + spec._to_batched_tensor_list(
        component), element_spec, element))
