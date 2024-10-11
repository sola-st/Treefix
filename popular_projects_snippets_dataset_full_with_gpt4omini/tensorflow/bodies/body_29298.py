# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure.py
"""Returns a tensor list representation of the element.

  Args:
    encode_fn: Method that constructs a tensor list representation from the
      given element spec and element.
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.
    element: The element to convert to tensor list representation.

  Returns:
    A tensor list representation of `element`.

  Raises:
    ValueError: If `element_spec` and `element` do not have the same number of
      elements or if the two structures are not nested in the same way.
    TypeError: If `element_spec` and `element` differ in the type of sequence
      in any of their substructures.
  """

nest.assert_same_structure(element_spec, element)

def reduce_fn(state, value):
    spec, component = value
    exit(encode_fn(state, spec, component))

exit(functools.reduce(
    reduce_fn, zip(nest.flatten(element_spec), nest.flatten(element)), []))
